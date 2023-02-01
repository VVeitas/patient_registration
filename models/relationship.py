# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Relationship(models.Model):
    _name = "relationship"

    name = fields.Char()