# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.picking_ids:
                for picking in self.picking_ids:
                    picking.write({'sale_order_id': self.id})

            if not order.invoice_ids:
                order._create_invoices()

            if order.invoice_ids:
                for invoice in order.invoice_ids:
                    invoice.write({'sale_order_id': self.id})
                    invoice.action_post()
        return res
