# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_delivery_carrier = fields.Boolean()
