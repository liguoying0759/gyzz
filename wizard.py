# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    # def _default_session(self):
    #     return self.env['res.partner'].browse(self._context.get('active_id'))

    def _default_sessions(self):
        return self.env['res.partner'].browse(self._context.get('active_ids'))

    # session_id = fields.Many2one('res.partner',
    #     string="partner", required=True,default=_default_session)

    session_ids = fields.Many2many('res.partner',
                                   string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2one('res.users', string="Attendees")

    @api.multi
    def subscribe(self):
        print(self._context)
        # self.session_id.user_id |= self.attendee_ids
        # return {}
        for session in self.session_ids:
            session.user_id |= self.attendee_ids