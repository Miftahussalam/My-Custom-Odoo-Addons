# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools import float_compare


class Picking(models.Model):
    _inherit = "stock.picking"

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', tracking=True)

    def validate_picking(self):
        """Set quantities automatically and validate the pickings."""
        for picking in self:
            picking.action_assign()
            for move in picking.move_lines.filtered(
                    lambda m: m.state not in ["done", "cancel"]
            ):
                rounding = move.product_id.uom_id.rounding
                if (
                        float_compare(
                            move.quantity_done,
                            move.product_qty,
                            precision_rounding=rounding,
                        )
                        == -1
                ):
                    for move_line in move.move_line_ids:
                        move_line.qty_done = move_line.product_uom_qty
            picking.with_context(skip_immediate=True).button_validate()
        return True
