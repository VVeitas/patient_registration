# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Relationship(models.Model):
    _name = "relationship"
    # _description = 'patient_registration.patient_registration'

    test = fields.Char()