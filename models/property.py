#-*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.api import depends


class Property(models.Model):
    _name = 'real_estate_ads.property'
    _description = 'Estate properties'

    def action_real_estate_ads_property_show_offers_action_window(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Offers',
            'res_model': 'real_estate_ads.property_offer',
            'view_mode': 'tree,form',
            'domain': [('property_id', '=', self.id)],
            'context': {'create': False}
    }

    name = fields.Char(string="Name", required=True)
    state = fields.Selection(
        string="Status",
        selection=[
            ('new', 'New'),
            ('received', 'Offer Received'),
            ('accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancel', 'Cancelled'),
        ],
        default='new'
    )
    type_id = fields.Many2one(
        comodel_name="real_estate_ads.property_type",
        string="Property Type"
    )
    tag_ids = fields.Many2many(
        comodel_name="real_estate_ads.property_tag",
        relation="property_tags_rel",
        column1="property_tag_id",
        column2="property_id",
        string="Tags"
    )

    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(streing="Best Offer", compute="_compute_best_offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(strling="Living Area(sqm)")
    facades = fields.Integer(strling="Facades")
    garage = fields.Boolean(strling="Garage", default=False)
    garden = fields.Boolean(strling="Garden", default=False)
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
    offer_ids = fields.One2many(
        comodel_name="real_estate_ads.property_offer",
        inverse_name="property_id",
        string="Offers"
    )
    sales_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesman"
    )
    buyer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Buyer",
        domain=[('is_company', '=', True)] # show only the companies
    )
    phone = fields.Char(
        string="Phone",
        related="buyer_id.phone"
    )
    offer_count = fields.Integer(
        string="Offer Count",
        compute="_compute_offer_count"
    )
    total_area = fields.Integer(
        string="Total Area",
        compute="_compute_total_area"
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    def action_sold(self):
        for rec in self:
            rec.state = "sold"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_offer = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_offer = 0

    def action_client_action_example(self):
        return {
            'type': 'ir.actions.client',
            #'tag': 'reload'  # this will reload the page
            #'tag': 'apps'  # this will open the odoo apps store
            'tag': 'display_notification',
            'params': {
                'title': 'A title',
                'message': 'A message for the notification',
                'type': 'success',  # success, warning, danger
                'sticky': False,  # True will make the notification sticky, false will make it disappear
            }
        }

    def action_url_action_example(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://odoo.com',
            'target': 'self' # self: abre url en la misma pestaña, new: abre url en una nueva pestaña
        }