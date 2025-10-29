from odoo import  fields, models, api
from datetime import timedelta


class Propertyoffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(string="Prix")
    status =  fields.Selection([
        ('accepted', 'Acceté'), ('refused', 'Refusé'),
    ], string="Status")
    partner_id = fields.Many2one('res.partner', string="Client")
    property_id = fields.Many2one('estate.property', string="Bien")
    validity = fields.Integer(string="Validity")
    deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse='_inverse_deadline')
    creation_date = fields.Date(string="Creation Date")

    @api.depends('creation_date', 'validity')
    def _compute_deadline(self):
        for record in self:
            if record.creation_date and record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)
            else:
                record.deadline = None

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.deadline - record.creation_date).days