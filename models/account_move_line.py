from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.depends('currency_id', 'company_id', 'move_id.date')
    def _compute_currency_rate(self):

        # ---------------------------------------
        # Extension function with create NC get TC from invoice
        # ---------------------------------------

        compute_currency_rate = super(AccountMoveLine, self)._compute_currency_rate()

        def get_rate_out_refund(from_currency, to_currency, company, date):
            return self.env['res.currency']._get_conversion_rate(
                        from_currency=from_currency,
                        to_currency=to_currency,
                        company=company,
                        date=date,
                    )
        for line in self:
            if line.move_id.move_type in ('in_refund', 'out_refund'):
                line.currency_rate = get_rate_out_refund(
                    from_currency=line.company_currency_id,
                    to_currency=line.currency_id,
                    company=line.company_id,
                    date=line.move_id.reversed_entry_id.invoice_date or line.move_id.date or fields.Date.context_today(line),
                )
        return compute_currency_rate
        # ---------------------------------------------------


