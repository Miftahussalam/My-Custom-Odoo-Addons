# -*- coding: utf-8 -*-
from odoo import http

# class FitsLatihanBootcamp(http.Controller):
#     @http.route('/fits_latihan_bootcamp/fits_latihan_bootcamp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fits_latihan_bootcamp/fits_latihan_bootcamp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fits_latihan_bootcamp.listing', {
#             'root': '/fits_latihan_bootcamp/fits_latihan_bootcamp',
#             'objects': http.request.env['fits_latihan_bootcamp.fits_latihan_bootcamp'].search([]),
#         })

#     @http.route('/fits_latihan_bootcamp/fits_latihan_bootcamp/objects/<model("fits_latihan_bootcamp.fits_latihan_bootcamp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fits_latihan_bootcamp.object', {
#             'object': obj
#         })