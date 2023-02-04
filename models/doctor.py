from odoo import models, fields, api, _

class Doctor(models.Model):
    _name = "doctor"

    partner_id = fields.Many2one('res.partner', required=True)
    name = fields.Char(related='partner_id.name')
    photo = fields.Image()

    education = fields.Char()
    specialization = fields.Text()
    weekday_doctor_working = fields.Selection(
        [('monday', _('Monday')), ('tuesday', _('Tuesday')), ('wednesday', _('Wednesday')), ('thursday', 'Thursday'), ('friday', 'Friday')], 
        default='monday'
    )
    visit_count = fields.Integer(compute='_compute_visit_count')

    def _compute_visit_count(self):
        for record in self:
            record.visit_count = 0
            record.visit_count = record.env['visit'].search_count([('doctor', '=', record.id)])
    
    def action_view_visit_count(self):
        return {
            'name': _('Doctor visit count'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'visit',
            'domain': [('doctor', '=', self.id)],
        }