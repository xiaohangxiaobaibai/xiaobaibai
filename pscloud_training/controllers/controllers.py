# -*- coding: utf-8 -*-
from odoo import http

# class ../user/pscloudTraining(http.Controller):
#     @http.route('/../user/pscloud_training/../user/pscloud_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../user/pscloud_training/../user/pscloud_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../user/pscloud_training.listing', {
#             'root': '/../user/pscloud_training/../user/pscloud_training',
#             'objects': http.request.env['../user/pscloud_training.../user/pscloud_training'].search([]),
#         })

#     @http.route('/../user/pscloud_training/../user/pscloud_training/objects/<model("../user/pscloud_training.../user/pscloud_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../user/pscloud_training.object', {
#             'object': obj
#         })