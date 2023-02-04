from odoo import models, fields, api, _
import datetime

class Visit(models.Model):
    _name = "visit"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    patient = fields.Many2one('patient', string='Patient', required=True)
    doctor = fields.Many2one('doctor', string='Doctor', required=True)
    start_time = fields.Datetime(string='Start time')
    end_time = fields.Datetime(string='End time')
    visit_duration = fields.Char(
        string='Visit duration', 
        compute='_compute_visit_duration',
    )
    diagnosed_disease = fields.Many2many('disease')
    supplies_and_quantities = fields.One2many('supplies', 'visit')
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, default=lambda self: self.env.company.currency_id.id)
    total_amount_spent = fields.Monetary(string='Total price amount of used supplies', compute='_compute_total_amount_spent', store=True, tracking=True)
    patient_symptoms = fields.Html()
    treatment_recommendations = fields.Html()
    visit_state = fields.Selection([('registration', 'Registration'), ('visit', 'Visit'), ('treatment', 'Treatment'), ('done', 'Done')], 
        default='registration', tracking=True
    )

    @api.depends('supplies_and_quantities')
    def _compute_total_amount_spent(self):
        """Compute total monetary amount of supplies and quantities."""
        for record in self:
            record.total_amount_spent = 0
            if record.supplies_and_quantities:
                record.total_amount_spent = sum([line.quantity * line.product_tmpl_id.list_price for line in record.supplies_and_quantities])

    @api.depends('start_time', 'end_time')
    def _compute_visit_duration(self):
        for record in self:
            record.visit_duration = False
            if record.start_time and record.end_time:
                record.visit_duration = str(record.end_time - record.start_time)

    def write(self, vals):
        res = super().write(vals)
        self.add_followers() # add patient or doctor to record followers
        return res

    @api.model_create_multi
    def create(self, vals):
        res = super().create(vals)
        res.add_followers() # add patient or doctor to record followers
        return res

    def add_followers(self):
        """If patient or doctor is not in followers, subscribe them."""
        for record in self:
            if record.patient and record.patient.partner_id.id not in record.message_partner_ids.ids:
                record.message_subscribe([record.patient.partner_id.id])
            if record.doctor and record.doctor.partner_id.id not in record.message_partner_ids.ids:
                record.message_subscribe([record.doctor.partner_id.id])

