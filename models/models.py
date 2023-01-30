# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class patient_registration(models.Model):
#     _name = 'patient_registration.patient_registration'
#     _description = 'patient_registration.patient_registration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
