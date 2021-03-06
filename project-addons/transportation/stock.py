# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Omar Castiñeira Saavedra
#    Copyright 2015 Comunitea Servicios Tecnológicos S.L.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    @api.multi
    @api.depends('move_lines.state', 'move_lines.picking_id',
                 'move_lines.product_id', 'move_lines.product_uom_qty',
                 'move_lines.product_uom')
    def _cal_weight(self):
        for picking in self:
            total_weight = total_weight_net = 0.00
            for move in picking.move_lines:
                if move.state != 'cancel':
                    total_weight += move.weight
                    total_weight_net += move.weight_net

            picking.weight = total_weight
            picking.weight_net = total_weight_net

    @api.model
    def _get_default_uom(self):
        uom_categ_id = self.env.ref('product.product_uom_categ_kgm')
        return self.env['product.uom'].search([('category_id', '=',
                                                uom_categ_id.id),
                                               ('factor', '=', 1)])[0]

    volume = fields.Float('Volume', copy=False)
    weight = fields.Float('Weight', compute='_cal_weight', multi=True,
                          digits_compute=dp.get_precision('Stock Weight'))
    weight_net = fields.Float('Net Weight', compute="_cal_weight",
                              digits_compute=dp.get_precision('Stock Weight'),
                              multi=True)
    carrier_tracking_ref = fields.Char('Carrier Tracking Ref', copy=False)
    number_of_packages = fields.Integer('Number of Packages', copy=False)
    weight_uom_id = fields.Many2one('product.uom', 'Unit of Measure',
                                    required=True, readonly="1",
                                    help="Unit of measurement for Weight",
                                    default=_get_default_uom)


class StockMove(models.Model):

    _inherit = "stock.move"

    @api.multi
    @api.depends('product_id', 'product_uom_qty', 'product_uom')
    def _cal_move_weight(self):
        for move in self:
            weight = weight_net = 0.00
            if move.product_id.weight > 0.00:
                converted_qty = move.product_qty
                weight = (converted_qty * move.product_id.weight)

                if move.product_id.weight_net > 0.00:
                    weight_net = (converted_qty * move.product_id.weight_net)

            move.weight = weight
            move.weight_net = weight_net

    @api.model
    def _get_default_uom(self):
        uom_categ_id = self.env.ref('product.product_uom_categ_kgm')
        return self.env['product.uom'].search([('category_id', '=',
                                                uom_categ_id.id),
                                               ('factor', '=', 1)])[0]

    weight = fields.Float('Weight', compute='_cal_move_weight', multi=True,
                          digits_compute=dp.get_precision('Stock Weight'),
                          store=True)
    weight_net = fields.Float('Net weight', compute='_cal_move_weight',
                              digits_compute=dp.get_precision('Stock Weight'),
                              store=True, multi=True)
    weight_uom_id = fields.Many2one('product.uom', 'Unit of Measure',
                                    required=True, readonly="1",
                                    help="Unit of Measure (Unit of Measure) "
                                         "is the unit of measurement for "
                                         "Weight", default=_get_default_uom)
