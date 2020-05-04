from odoo import api, fields, models, osv


class PreventCreateNewProductOnSalesOrderLines(osv.osv.Model):
    _inherit = 'sale.order'
