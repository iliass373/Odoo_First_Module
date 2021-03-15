# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

"""
class ModuleTest(http.Controller):
    @http.route('/module_test/module_test/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/module_test/module_test/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('module_test.listing', {
            'root': '/module_test/module_test',
            'objects': http.request.env['module_test.module_test'].search([]),
        })

    @http.route('/module_test/module_test/objects/<model("module_test.module_test"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('module_test.object', {
            'object': obj
        })  
"""


class Controller(http.Controller):

    @http.route(['/my/sessions/'], type='http', auth='user', website=True)
    def check_sessions(self):
        sessions = request.env['openacademy.sessions'].sudo().search([])
        professeurs = request.env['openacademy.prof'].sudo().search([])
        student = request.env['openacademy.student'].sudo().search([])
        #tickets_count = len(request.env['helpdesk.ticket'].search(domain))
        return request.render('module_test.session_template', {   # Nom du module. nom template
            'sessions': sessions,
            'professeurs': professeurs,
            'students': student,
        })

    @http.route(["/my/sessions/<int:session_id>"], type='http', auth="public", website=True)
    def show_sessions(self, session_id=None, access_token=None, **kw):

        print(request.env["openacademy.sessions"].browse(request.env.uid).id)
        sessions = request.env['openacademy.sessions'].sudo().search([])
        professeurs = request.env['openacademy.prof'].sudo().search([])
        student = request.env['openacademy.student'].sudo().search([])
        values = request.env['openacademy.sessions']
        return request.render('module_test.tickets_followup',values)