# -*- coding: utf-8 -*-
# from odoo import http


# class OdooOlamundo(http.Controller):
#     @http.route('/olamundo/olamundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/olamundo/olamundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('olamundo.listing', {
#             'root': '/olamundo/olamundo',
#             'objects': http.request.env['olamundo.olamundo'].search([]),
#         })

#     @http.route('/olamundo/olamundo/objects/<model("olamundo.olamundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('olamundo.object', {
#             'object': obj
#         })
