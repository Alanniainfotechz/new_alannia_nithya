# See LICENSE file for full copyright and licensing details.

{
    'name': 'Repeat the saless order from portal',
    'version': '15.0.1.0.0',
    'summary': "For created repeat the sales order from existing ale order from portal ",
    'license': 'AGPL-3',
    'author': 'Nithyal',
    'price': 10.18,
    'currency': 'USD',
    'depends': [
        'website_sale','sale_management'],
    'data': [
        'views/inherit_sale_port_temp.xml',
        'views/inherit_sale_view.xml',
        'views/show _origin_sale_template.xml',

    ],
    'images':['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
}
