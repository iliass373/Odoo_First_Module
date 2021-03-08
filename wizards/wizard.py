

from odoo import models, fields, api, _


class Wizard(models.TransientModel):
    _name = "create.profwizzard"
    def _default_session(self):
        prof = self.env["openacademy.session"].browse(self._context.get("active_ids"))

    sess_id = fields.Many2one("openacademy.session", "user_name")
    notes = fields.Text(string="Notes")
    attende_id = fields.Many2many('res.partner', string="Attendees")

    def create_prof_wizzard_button(self):
        for session in self.sess_id:
            session.attende_id |= self.attende_id
        return {}
