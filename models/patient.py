from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

class Patient(models.Model):
    _name = "patient"

    partner_id = fields.Many2one('res.partner')
    birthday = fields.Date()
    age = fields.Integer(store=True, compute='_compute_age')
    relatives = fields.One2many('relatives', 'patient')
    visits = fields.One2many('visit', 'patient')

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            record.age = False
            if record.birthday:
                difference_in_years = relativedelta(date.today(), record.birthday).years
                record.age = difference_in_years