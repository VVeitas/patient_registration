# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPatient(models.Model):
    _name = 'res.patient'

    test = fields.Char()