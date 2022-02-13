# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _


class PosOrder(models.Model):
    _inherit = "pos.order"

    payment_method_id = fields.Many2one(related='payment_ids.payment_method_id', store=True)
