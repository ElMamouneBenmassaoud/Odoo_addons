# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/(http.Controller):
#     @http.route('//mnt/extra-addons///mnt/extra-addons//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons///mnt/extra-addons//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/.listing', {
#             'root': '//mnt/extra-addons///mnt/extra-addons/',
#             'objects': http.request.env['/mnt/extra-addons/./mnt/extra-addons/'].search([]),
#         })

#     @http.route('//mnt/extra-addons///mnt/extra-addons//objects/<model("/mnt/extra-addons/./mnt/extra-addons/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/.object', {
#             'object': obj
#         })
