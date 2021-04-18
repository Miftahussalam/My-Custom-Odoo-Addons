from odoo import models, fields


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'
    divisi_id = fields.Many2one(string='Divisi', related='employee_id.divisi_id', store=True)
