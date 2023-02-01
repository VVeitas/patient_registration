from odoo import models, fields, api, _

class Doctor(models.Model):
    _name = "doctor"

    partner_id = fields.Many2one('res.partner')
    photo = fields.binary()
    education = fields.Char()
    specialization = fields.Text()
    weekday_doctor_working = fields.Selection(
        [('monday', _('Monday')), ('tuesday', _('Tuesday')), ('wednesday', _('Wednesday')), ('thursday', 'Thursday'), ('friday', 'Friday')], 
        default='monday',
    )

    def action_view_visit_count(self):
        return {
            'name': _('Doctor visit count'),
            'type': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'visit',
            'domain': [('doctor', '=', self.id)],
        }