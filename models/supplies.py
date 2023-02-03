# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Supplies(models.Model):
    _name = "supplies"
    
    visit = fields.Many2one('visit')
    product_tmpl_id = fields.Many2one('product.template', required=True)
    quantity = fields.Integer(digits='Product Unit of Measure', required=True)
    