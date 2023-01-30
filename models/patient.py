from odoo import models, fields, api
import datetime

class Patient(models.Model):
    _name = "patient"

    partner_id = fields.Many2one('res.partner')
    birthday = fields.Date()
    age = fields.Integer(store=True, compute='_compute_age')
    registrations = fields.One2many('visit', 'patient')

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            record.age = datetime.datetime.now() - record.birthday