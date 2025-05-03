#-*- coding: utf-8 -*-
from Crypto.Util.number import inverse
from fsspec.registry import default
from odoo.exceptions import ValidationError

from odoo import fields, models, api
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = 'real_estate_ads.property_offer'
    _description = 'Estate Property Offers'

    name = fields.Char(
        string="Description",
        compute="_compute_name"
    )

    price = fields.Float(string="Price")
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        string="Status"
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer"
    )
    property_id = fields.Many2one(
        comodel_name="real_estate_ads.property",
        string="Property"
    )
    validity = fields.Integer(string="Validity", default=7)
    deadline = fields.Date(
        string="Deadline",
        compute="_compute_deadline",
        inverse="_inverse_deadline"
    )

    @api.model
    def set_create_date(self):
        return fields.Date.today()

    creation_date = fields.Date(string="Creation Date", default=set_create_date)


    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_deadline(self):
        for rec in self:
            if rec.creation_date and rec.deadline:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False

    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.creation_date:
                raise ValueError("Deadline must be greater than creation date")

    @api.depends('partner_id', 'property_id')
    def _compute_name(self):
        for rec in self:
            if rec.partner_id and rec.property_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name}"
            else:
                rec.name = False

    def action_accept_offer(self):
        if self.property_id:
            self._validate_accepted_offer()
            self.property_id.state = "accepted"
            # self.property_id.selling_price = self.price
            self.property_id.write({
                'selling_price': self.price,
                'state': 'accepted'
            })
        self.status = "accepted"

    def _validate_accepted_offer(self):
        accepted_offers_ids = self.env['real_estate_ads.property_offer'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted')
        ])
        if accepted_offers_ids:
            raise ValidationError("There is already an accepted offer for this property")

    def action_decline_offer(self):
        self.status = "refused"
        if all(self.property_id.offer_ids.mapped('status')):
            # self.property_id.selling_price = 0
            self.property_id.write({
                'selling_price': 0,
                'state': 'received'
            })

    def extend_offer_deadline(self):
        active_ids = self._context.get('active_ids', [])
        if active_ids:
            offer_ids = self.env['real_estate_ads.property_offer'].browse(active_ids)
            for offer in offer_ids:
                offer.validity = 10
