# -*- coding: utf-8 -*-
# © 2015-2016 Odoo S.A.
# © 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Website Portal for Sales (Backported From v10)',
    'category': 'Website',
    'summary': 'Add your sales document in the frontend portal (sales order, '
               'quotations, invoices)',
    'version': '9.0.1.0.0',
    'depends': [
        'sale',
        'website_portal_v10',
        'website_payment_v10',
    ],
    'data': [
        'views/templates.xml',
    ],
    'demo': [
        'data/demo.xml'
    ],
    'installable': True,
}
