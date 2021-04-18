from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class PengajuanSppd(models.Model):
    _name = 'report.pengajuan.sppd'
    _description = 'Pengajuan SPPD'

    @api.model
    def _employee_get(self):
        emp = self.env['hr.employee'].search([('user_id', '=', self._uid)], limit=1)
        if emp:
            return emp

    name = fields.Char(string='No SPPD', default="New", copy=False)
    wilayah = fields.Char(string='Wilayah')
    note = fields.Text(string='Maksud Utama')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id, readonly=True)
    date = fields.Date(string='Tanggal Pengajuan', default=fields.Date.context_today)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee', default=_employee_get)
    manager_id = fields.Many2one(string='Manager', related='employee_id.parent_id', store=True)
    sppd_line_ids = fields.One2many('pengajuan.sppd.line', 'sppd_id', string='Line SPPD')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('approve', 'Approved'),
        ('convert_to_expense', 'Convert Expense'),
        ('refuse', 'Refused'),
        ('done', 'Done'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')
    total = fields.Float(string='Total', compute='get_total')

    expenses_id = fields.Many2one('hr.expense.sheet', string='Expenses Report')
    lphd_ids = fields.Many2one('report.lphd', string='LPHD')

    @api.depends('sppd_line_ids.sub_total')
    def get_total(self):
        for line in self.sppd_line_ids:
            self.total += line.sub_total

    @api.multi
    def unlink(self):
        for x in self:
            if x.state != 'draft':
                raise UserError(_('You cannot delete a SPPD on another state draft'))
        super(PengajuanSppd, self).unlink()

    def create_expense(self):
        expense_sheet = self.env['hr.expense.sheet']
        expense = self.env['hr.expense']
        for sppd in self:
            exp = expense_sheet.create({
                'name': sppd.name + sppd.wilayah,
                'employee_id': sppd.employee_id.id
            })

            for line in sppd.sppd_line_ids:
                expense.create({
                    'product_id': line.product_id.id,
                    'name': line.product_id.name,
                    'unit_amount': line.amount,
                    'quantity': line.qty,
                    'date': sppd.date,
                    'sheet_id': exp.id
                })
            sppd.expenses_id = exp.id

    def create_lphd(self):
        lphd_model = self.env['report.lphd']
        realisasi_biaya_line = self.env['realisasi.biaya.line']
        for sppd in self:
            exp = lphd_model.create({
                'sppd_ids': sppd.id,
            })

            for line in sppd.sppd_line_ids:
                realisasi_biaya_line.create({
                    'jenis_biaya': line.product_id.id,
                    'lphd_id': exp.id
                })
            sppd.lphd_ids = exp.id

    def action_submit(self):
        if self.name == 'New':
            self.name = self.env['ir.sequence'].next_by_code('sppd')
        self.state = 'submit'

    def action_approve(self):
        self.state = 'approve'

    def action_convert_to_expense(self):
        self.create_expense()
        self.state = 'convert_to_expense'

    def action_refuse(self):
        self.state = 'refuse'

    def action_done(self):
        self.create_lphd()
        self.state = 'done'

    def action_set_draft(self):
        self.state = 'draft'


class SppdLine(models.Model):
    _name = 'pengajuan.sppd.line'
    _description = 'Pengajuan SPPD Line'

    product_id = fields.Many2one('product.product', string='Product', domain=[('can_be_expensed', '=', True)])
    qty = fields.Float(string='Quantity')
    amount = fields.Float(string='Amount')
    sub_total = fields.Float(string='Subtotal', compute='_get_subtotal')
    note = fields.Char(string='Keterangan')
    sppd_id = fields.Many2one('report.pengajuan.sppd', string='SPPD')

    @api.depends('qty', 'amount')
    def _get_subtotal(self):
        for line in self:
            line.sub_total = line.qty * line.amount
