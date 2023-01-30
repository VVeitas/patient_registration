from odoo import models, fields, api

class Disease(models.Model):
    _name = "disease"

    code = fields.Char()
    name = fields.Char()
    description = fields.Html()
    symptoms = fields.Char()
    treatment_recommendations = fields.Char()