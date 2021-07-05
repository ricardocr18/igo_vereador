# -*- coding: utf-8 -*-
# from odoo import http


# class ..\apps\igoVereador(http.Controller):
#     @http.route('/..\apps\igo_vereador/..\apps\igo_vereador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/..\apps\igo_vereador/..\apps\igo_vereador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('..\apps\igo_vereador.listing', {
#             'root': '/..\apps\igo_vereador/..\apps\igo_vereador',
#             'objects': http.request.env['..\apps\igo_vereador...\apps\igo_vereador'].search([]),
#         })

#     @http.route('/..\apps\igo_vereador/..\apps\igo_vereador/objects/<model("..\apps\igo_vereador...\apps\igo_vereador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('..\apps\igo_vereador.object', {
#             'object': obj
#         })
