from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

class Patient(models.Model):
    _name = "patient"

    partner_id = fields.Many2one('res.partner', required=True)
    name = fields.Char(related='partner_id.name')
    birthday = fields.Date()
    age = fields.Integer(store=True, compute='_compute_age')
    relatives = fields.One2many('relatives', 'patient')
    visits = fields.One2many('visit', 'patient')
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, default=lambda self: self.env.company.currency_id.id)
    patient_total_amount = fields.Monetary(string='Total price amount of used supplies', compute='_compute_patient_total_amount')
    visit_count = fields.Integer(compute='_compute_visit_count')

    def _compute_visit_count(self):
        for record in self:
            record.visit_count = 0
            record.visit_count = record.env['visit'].search_count([('patient', '=', record.id)])

    @api.depends('partner_id', 'visits')
    def _compute_patient_total_amount(self):
        for record in self:
            record.patient_total_amount = 0
            if record.visits:
                record.patient_total_amount = sum(record.visits.mapped('total_amount_spent'))

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            record.age = False
            if record.birthday:
                difference_in_years = relativedelta(date.today(), record.birthday).years
                record.age = difference_in_years

    def action_view_patient_amount_total(self):
        return {
            'name': _('Patient amount total'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'visit',
            'domain': [('patient', '=', self.id)],
            'context': {'search_default_patient': 1},
        }

    def action_view_visit_count(self):
        return {
            'name': _('Doctor visit count'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'visit',
            'domain': [('doctor', '=', self.id)],
        }