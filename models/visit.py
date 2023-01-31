from odoo import models, fields, api
import datetime

class Visit(models.Model):
    _name = "visit"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient = fields.Many2one('patient', string='Patient')
    doctor = fields.Many2one('doctor', string='Doctor')
    start_time = fields.Datetime(string='Start time')
    end_time = fields.Datetime(string='End time')
    visit_duration = fields.Datetime(
        string='Visit duration', 
        compute='_compute_visit_duration',
        store=True,
    )
    diagnosed_disease = fields.Many2many('disease')
    supplies_and_quantities = fields.One2many('supplies', 'visit')
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, default=lambda self: self.env.company.currency_id.id)
    total_amount = fields.Monetary(string='Total price amount of used supplies', compute='_compute_total_amount', store=True)
    patient_symptoms = fields.Html()
    treatment_recommendations = fields.Html()
    visit_state = fields.Selection([('registration', 'Registration'), ('visit', 'Visit'), ('treatment', 'Treatment'), ('done', 'Done')], 
        default='registration',
    )

    @api.depends('supplies_and_quantities')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = 0
            if record.supplies_and_quantities:
                record.total_amount = sum([line.quantity * line.product_tmpl_id.list_price for line in record.supplies_and_quantities])

    @api.depends('start_time', 'end_time')
    def _compute_visit_duration(self):
        for record in self:
            record.visit_duration = False
            if record.start_time and record.end_time:
                record.visit_duration = record.end_time - record.start_time