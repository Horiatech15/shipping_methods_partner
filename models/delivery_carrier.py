# -*- coding: utf-8 -*-

from odoo import fields, models


class DeliveryCarrierInherit(models.Model):
    _inherit = 'delivery.carrier'

    partner_id = fields.Many2one('res.partner')

    def action_create_partner(self):
        if not self.partner_id:
            partner_id = self.env['res.partner'].create({
                'name': '%s - %s' % (self.name, self.state_ids[0].name),
                'country_id': self.country_ids[0].id,
                'state_id': self.state_ids[0].id,
                'type': 'delivery',
                'company_type': 'company',
                'is_delivery_carrier': True,
            })
            self.partner_id = partner_id.id


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def set_delivery_line(self, carrier, amount):
        self._remove_delivery_line()
        for order in self:
            order.carrier_id = carrier.id
            if carrier.partner_id:
                order.partner_shipping_id = carrier.partner_id.id
            order._create_delivery_line(carrier, amount)
        return True

