from odoo import models, fields, api


class AccountBanckStatmentLine(models.Model):
    _inherit = 'account.bank.statement.line'

    l10n_pe_base_account_payment_method_id = fields.Many2one('l10n_pe_base_account.tabla_01', string='Medio de pago [tabla 01 sunat]')
    l10n_pe_base_account_bank_transaction_number = fields.Char('Número de la transacción bancaria')
