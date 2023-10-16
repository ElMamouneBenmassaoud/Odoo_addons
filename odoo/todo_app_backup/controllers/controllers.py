# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/todoApp(http.Controller):
#     @http.route('//mnt/extra-addons/todo_app//mnt/extra-addons/todo_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/todo_app//mnt/extra-addons/todo_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/todo_app.listing', {
#             'root': '//mnt/extra-addons/todo_app//mnt/extra-addons/todo_app',
#             'objects': http.request.env['/mnt/extra-addons/todo_app./mnt/extra-addons/todo_app'].search([]),
#         })

#     @http.route('//mnt/extra-addons/todo_app//mnt/extra-addons/todo_app/objects/<model("/mnt/extra-addons/todo_app./mnt/extra-addons/todo_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/todo_app.object', {
#             'object': obj
#         })
