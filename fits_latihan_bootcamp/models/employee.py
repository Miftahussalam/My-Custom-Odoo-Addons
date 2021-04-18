# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrDivisi(models.Model):
    _name = 'hr.divisi'
    _description = 'Divisi'

    name = fields.Char(string='Nama Divisi')
    desc = fields.Char(string='Keterangan')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    divisi_id = fields.Many2one('hr.divisi', string='Divisi')
    nik = fields.Char(string='NIK')
    tgl_bergabung = fields.Date(string='Tanggal Bergabung')
    agama = fields.Selection([('Islam', 'Islam')])
    riwayat_ids = fields.One2many('riwayat.pekerjaan', 'employee_id', string='Riwayat')


class RiwayatPekerjaan(models.Model):
    _name = 'riwayat.pekerjaan'
    _description = 'Riwayat Pekerjaan'

    mulai_bekerja = fields.Char(string="Tahun Mulai Bekerja")
    selesai_bekerja = fields.Char(string="Selesai Bekerja")
    nama_perusahaan = fields.Char(string="Nama Perusahaan")
    res_partner_id = fields.Many2one('res.partner', string="Company")
    jabatan = fields.Char(string="Jabatan")
    employee_id = fields.Many2one('hr.employee', string="Employee")
