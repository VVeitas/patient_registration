from odoo import models, fields, api

class Doctor(models.Model):
    _name = "doctor"

    partner_id = fields.Many2one('res.partner')