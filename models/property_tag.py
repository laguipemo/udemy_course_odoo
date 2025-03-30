#-*- coding: utf-8 -*-
from odoo import fields, models, api


class PropertyTag(models.Model):
    _name = 'real_estate_ads.property_tag'
    _description = 'Tag assigned to a property'

    name = fields.Char(string="Name", required=True)
