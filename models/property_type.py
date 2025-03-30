#-*- coding: utf-8 -*-
from odoo import fields, models, api


class PropertyType(models.Model):
    _name = 'real_estate_ads.property_type'
    _description = 'The type of property'

    name = fields.Char(string="Name", required=True)
