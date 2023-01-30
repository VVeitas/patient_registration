# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Relatives(models.Model):
    _name = "relatives"
    
    partner_id = fields.Many2one('res.partner')
    relationship_type = fields.Many2one('relationship')
    patient = fields.Many2one('res.partner')