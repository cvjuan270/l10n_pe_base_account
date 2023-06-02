from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        for rec in self:
            if rec.move_type in ('out_refund', 'in_refund'):
                # Verify that there is an invoice
                if not rec.reversed_entry_id:
                    raise UserError("No se puede crear Nota de crédito sin Factura afecta")
                # Check outstanding balance
                if rec.reversed_entry_id.amount_residual == 0:
                    raise UserError(f'No se puede crear Nota de Crédito; Saldo de la factura {rec.reversed_entry_id.name} es: 0.00')
                if rec.reversed_entry_id.amount_residual < rec.amount_total:
                    raise UserError(f"""No se puede crear Nota de Crédito\n 
                                    - El monto de NC excede el saldo de la Factura. \n
                                    - {rec.reversed_entry_id.name}Importe Adeudado: {rec.reversed_entry_id.amount_residual}""")

        return super()._post()
    