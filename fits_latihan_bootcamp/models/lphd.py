from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class Lphd(models.Model):
    _name = 'report.lphd'
    _description = 'LPHD'

    no_lphd = fields.Char(string='No LPHD', default='New', copy=False)
    sppd_ids = fields.Many2one('report.pengajuan.sppd', string='SPPD')
    nama_karyawan = fields.Many2one(string='Nawa Karyawan', related='sppd_ids.employee_id')
    manager = fields.Many2one(string='Manager', related='sppd_ids.manager_id')
    departement = fields.Many2one(string='Departement', related='nama_karyawan.department_id')

    periode_dari = fields.Date(string='Periode Dari')
    periode_sampai = fields.Date(string='Periode Sampai')

    maksud_utama = fields.Char(string='Maksud Utama')
    wilayah_dikunjungi = fields.Char(string='Wilayah yang di kunjungi')

    aktivitias = fields.Html(string='Aktivitas')
    total = fields.Float(string='Total', compute='_get_total')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('approve_manager', 'Approve Manager'),
        ('approve', 'Approved'),
        ('refuse', 'Refused'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')
    realisasi_biaya_ids = fields.One2many('realisasi.biaya.line', 'lphd_id', string='Line LPHD')

    @api.depends('realisasi_biaya_ids.sub_total')
    def _get_total(self):
        for line in self.realisasi_biaya_ids:
            self.total += line.sub_total

    def action_submit(self):
        if self.no_lphd == 'New':
            self.no_lphd = self.env['ir.sequence'].next_by_code('lphd')
        self.state = 'submit'

    def action_approve_manager(self):
        self.state = 'approve_manager'

    def action_approve(self):
        self.state = 'approve'

    def action_refused(self):
        self.state = 'refuse'

    def action_set_draft(self):
        self.state = 'draft'


class RealisasiBiaya(models.Model):
    _name = 'realisasi.biaya.line'
    _description = 'Realisasi Biaya'

    jenis_biaya = fields.Many2one('product.product', string='Jenis Biaya', domain=[('can_be_expensed', '=', True)])
    biaya_hari_1 = fields.Float(string='Biaya Hari-1')
    biaya_hari_2 = fields.Float(string='Biaya Hari-2')
    biaya_hari_3 = fields.Float(string='Biaya Hari-3')
    biaya_hari_4 = fields.Float(string='Biaya Hari-4')
    biaya_hari_5 = fields.Float(string='Biaya Hari-5')
    sub_total = fields.Float(string='Sub Total', compute='_get_subtotal')
    lphd_id = fields.Many2one('report.lphd', string='LPHD')

    @api.depends('biaya_hari_1', 'biaya_hari_2', 'biaya_hari_3', 'biaya_hari_4', 'biaya_hari_5')
    def _get_subtotal(self):
        for line in self:
            line.sub_total = line.biaya_hari_1 + line.biaya_hari_2 + line.biaya_hari_3 + line.biaya_hari_4 + line.biaya_hari_5
