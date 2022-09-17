# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import dropbox
import os

class WebsiteSale(WebsiteSale):

    @http.route(['/order/repeat'], type='http', auth='user', website=True)
    def repeat_so_portal(self, redirect=None, **post):
        so_id = post.get('order_id')
        so_name = post.get('name')
        order = request.env['sale.order'].browse(int(so_id))
        sale_order = request.website.sale_get_order(force_create=True)
        if sale_order.state != 'draft':
            request.session['sale_order_id'] = None
            sale_order = request.website.sale_get_order(force_create=True)
        for line in order.order_line:
            sale_order._cart_update(line.product_id.id,int(line.product_uom_qty),int(line.product_uom_qty))
        sale_order.reference_sale = so_name
        sale_order.repeat_order = True

        return request.redirect('/shop/cart')

    @http.route(['/customer/submit/salename'], type='http', auth='user', csrf=False, website=True)
    def customer_submit_sale_name(self, redirect=None, **post):
        order_id = int(post.get('order_id'))
        sale_name = post.get('sale_name')
        sal_order = request.env['sale.order'].browse(order_id)
        if sal_order:
            sal_order.sudo().sale_ref_name = sale_name
            print('reeeeeeeeeefvvfbdbdfhdb0',sal_order.sale_ref_name)
        return request.redirect('/shop/cart')
