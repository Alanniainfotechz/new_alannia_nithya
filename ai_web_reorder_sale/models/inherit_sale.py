    # See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models,_
import dropbox
import os

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reference_sale = fields.Char('Original SO', readonly=1)
    repeat_order = fields.Boolean('Repeated Order')
    sale_ref_name = fields.Char('Ref Name', readonly=True)





