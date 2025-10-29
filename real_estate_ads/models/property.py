from odoo import fields, models, api

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string="Nom", required=True)
    state = fields.Selection([
        ('new', "New"),
        ('received', 'Offer Received'),
        ('accepted', 'Accepted'),
        ('sold', 'Sold'),
        ('cancel',"Canceled")
    ],default='new', string="Status")
    type_id = fields.Many2one('estate.property.type', string="Type", required=True)
    tag_ids = fields.Many2many('estate.property.tag', string="Etiquete")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Code Postal")
    date_availability = fields.Date(string="Validité")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Meilleurs Offre")
    selling_price = fields.Float(string="Prix de Vente")
    bedrooms = fields.Integer(string="Pièces")
    living_area = fields.Integer(string="Surface (sqm)")
    facades = fields.Integer(string="Façades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Jardin", default=False)
    garden_area = fields.Integer(string="Surface Jardin (sqm)")
    garden_orientation = fields.Selection([
        ('north', 'Nord'), ('south', 'Sud'), ('east', 'Est'), ('west', 'Ouest'),
    ],
        string="Orientation du jardin", default='north')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offres")

    sales_id = fields.Many2one('res.users', string="Vendeurs")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', True)])
    phone = fields.Char(string="Phone", related='buyer_id.phone')

    @api.onchange('living_area', 'garden_area')
    def _compute_total_area(self):
            self.total_area = self.living_area + self.garden_area

    total_area = fields.Integer(string="Espace Total", compute=_compute_total_area)

    def action_sold(self):
        self.state = 'sold'
    def action_cancel(self):
        self.state = 'canceled'

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Type de bien'

    name = fields.Char(string="Nom", required=True)

class PropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char(string="Nom", required=True)