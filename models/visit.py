from odoo import models, fields, api
import datetime

class Visit(models.Model):
    _name = "visit"

    patient = fields.Many2one('patient', string='Patient')
    doctor = fields.Many2one('doctor', string='Doctor')
    start_time = fields.Datetime(string='Start time')
    end_time = fields.Datetime(string='End time')
    visit_duration = fields.Datetime(
        string='Visit duration', 
        compute='_compute_visit_duration',
        store=True,
    )
    diagnosed_disease = fields.Many2many('')

    @api.depends('start_time', 'end_time')
    def _compute_visit_duration(self):
        for record in self:
            record.visit_duration = False
            if record.start_time and record.end_time:
                record.visit_duration = record.end_time - record.start_time