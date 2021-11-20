from odoo import models


class SalesDetailsXlsx(models.AbstractModel):
    _name = 'report.pos_sales_details_advanced_report.report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objs):
        report_name = 'Sales Details'
        sheet = workbook.add_worksheet(report_name)
        bold = workbook.add_format({'bold': True})
        sheet.set_column('A:A', 25)
        sheet.set_column('B:B', 8)
        sheet.set_column('C:C', 5)
        sheet.set_column('D:D', 12)
        sheet.set_column('E:E', 12)
        sheet.set_column('F:F', 10)
        sheet.set_column('G:G', 12)
        sheet.set_column('H:H', 12)
        sheet.set_column('I:I', 6)
        sheet.set_column('J:J', 7)

        row_information = 0
        col = 0
        row_line = 9

        sheet.write(row_information, col, 'POS Sales Details Report', bold)
        sheet.write(row_information + 1, col, 'Date Start', bold)
        sheet.write(row_information + 2, col, 'End Date', bold)

        sheet.write(row_information + 4, col, 'Total Cost', bold)
        sheet.write(row_information + 5, col, 'Total Sales', bold)
        sheet.write(row_information + 6, col, 'Total Profit', bold)
        sheet.write(row_information + 7, col, 'Percentage Profit', bold)

        sheet.write(row_information + 9, col + 0, 'Product', bold)
        sheet.write(row_information + 9, col + 1, 'Quantity', bold)
        sheet.write(row_information + 9, col + 2, 'UoM', bold)
        sheet.write(row_information + 9, col + 3, 'Cost Price', bold)
        sheet.write(row_information + 9, col + 4, 'Price Unit', bold)
        sheet.write(row_information + 9, col + 5, 'Discount', bold)
        sheet.write(row_information + 9, col + 6, 'Total Cost', bold)
        sheet.write(row_information + 9, col + 7, 'Total Sale', bold)
        sheet.write(row_information + 9, col + 8, 'Profit', bold)
        sheet.write(row_information + 9, col + 9, '% Profit', bold)

        for obj in objs:
            sheet.write(row_information + 1, col + 1, obj._get_report_values(self, data=data)['date_start'])
            sheet.write(row_information + 2, col + 1, obj._get_report_values(self, data=data)['date_stop'])
            sheet.write(row_information + 4, col + 1, obj._get_report_values(self, data=data)['total_costs'])
            sheet.write(row_information + 5, col + 1, obj._get_report_values(self, data=data)['total_paid'])
            sheet.write(row_information + 6, col + 1, obj._get_report_values(self, data=data)['total_profit'])
            sheet.write(row_information + 7, col + 1, obj._get_report_values(self, data=data)['percentage_profit'])

            for line in obj._get_report_values(self, data=data)['products']:
                row_line += 1
                sheet.write(row_line, col, line['product_name'])
                sheet.write(row_line, col + 1, line['quantity'])
                sheet.write(row_line, col + 2, line['uom'] if line['uom'] else 'Units')
                sheet.write(row_line, col + 3, line['cost'])
                sheet.write(row_line, col + 4, line['price_unit'])
                sheet.write(row_line, col + 5, line['discount'] if line['discount'] else 0)
                sheet.write(row_line, col + 6, line['total_cost'])
                sheet.write(row_line, col + 7, line['total_sale'])
                sheet.write(row_line, col + 8, line['profit'])
                sheet.write(row_line, col + 9, line['percentage'])
