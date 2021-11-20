# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosDetails(models.TransientModel):
    _inherit = 'pos.details.wizard'

    def generate_report_excel(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date, 'config_ids': self.pos_config_ids.ids}
        return self.env.ref('pos_sales_details_advanced_report.sale_details_report_xlsx').report_action([], data=data)
