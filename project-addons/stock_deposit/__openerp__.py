# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Pexego Sistemas Informáticos All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@pexego.es>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Stock deposit',
    'version': '1.0',
    'category': 'product',
    'description': """Manage deposit of goods in a customer location""",
    'author': 'Pexego Sistemas Informáticos',
    'website': 'www.pexego.es',
    'depends' : ['base', 'sale', 'sale_stock', 'stock_reserve_sale',
                 'email_template_followers'],
    'data' : ['wizard/stock_invoice_deposit.xml',
              'stock_data.xml', 'stock_deposit.xml', 'res_partner_view.xml',
              'security/ir.model.access.csv', 'sale_view.xml',
              'data/stock_deposit_data.xml'],
    'installable': True
}
