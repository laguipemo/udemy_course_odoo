#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Property(models.Model):
    _name = 'real_estate_ads.property'
    _description = 'Estate properties'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date", readonly=True)
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(streing="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(strling="Living Area(sqm)")
    facades = fields.Integer(strling="Facades")
    garage = fields.Integer(strling="Garage", default=False)
    garden = fields.Integer(strling="Garden", default=False)
    garden_area = fields.Integer(strling="Garden Area(sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        default='north'
    )
