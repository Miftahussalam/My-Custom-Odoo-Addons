# -*- coding: utf-8 -*-
{
    'name': "POS Sales Details Advance Report",

    'summary': """
        Print report in PDF or Excel file,
        And more useful informations in POS Sales Details report,
        """,

    'description': """
        Print report in PDF or Excel file,
        And add cost price, sales prices, profit and percentage profit to POS Sales Details report,
        it also add information about total cost, total sales, total profit and total percentage profit.
    """,

    'author': "Tri Nanda",
    'website': "https://github.com/trinanda",
    'images': ['static/description/icon.png'],
    'category': 'Point of Sale',
    "price": 10.00,
    "currency": "USD",
    'version': '14.0.0.0.1',
    'application': False,
    "license": "AGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_salesdetails.xml',
        'views/point_of_sale_report.xml',
        'wizard/pos_details.xml',
    ],
}
