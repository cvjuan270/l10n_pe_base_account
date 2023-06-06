from odoo import models, fields, api


class Tabla01(models.Model):
    _name = 'l10n_pe_base_account.tabla_01'
    _description = 'Tabla 1: Tipo de medio de pago'

    code = fields.Char('Código')
    name = fields.Char('Descripción')

    @api.depends('code', 'name')
    def name_get(self):
        res = []
        for record in self:
            name = '[' + record.code + '] ' + record.name
            res.append((record.id, name))
        return res
