{
    'name': "fits_latihan_bootcamp",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "da Ti Soft Consulting",
    'website': "https://github.com/trinanda",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR, Expense',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_expense'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/employee_views.xml',
        'views/perjalanan_dinas_view.xml',
        'views/pengajuan_sppd_view.xml',
        'views/lphd_view.xml',
        'views/hr_expense_view.xml',
        'report/report_sppd.xml',
        'report/report_lphd.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
# -*- coding: utf-8 -*-
