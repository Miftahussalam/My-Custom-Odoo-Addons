from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', tracking=True)

    def _compute_amount(self):
        res = super(AccountMove, self)._compute_amount()
        for rec in self:
            self.check_payment_state(rec)
        return res

    def check_payment_state(self, account_move_id):

        stock_picking = self.env['stock.picking'].search(
            [('sale_order_id', '=', account_move_id.sale_order_id.id),
             ('state', "in", ("draft", "confirmed", "assigned"))])

        if account_move_id.payment_state == 'paid':
            if stock_picking:
                stock_picking.validate_picking()
