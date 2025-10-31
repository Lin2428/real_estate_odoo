from odoo import models, fields, api


class InvoiceStage(models.Model):
    _name = "invoice.stage"
    _description = "Invoice Stage"

    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=5)
    last_stage = fields.Boolean("Last Stage", default=False)
    color = fields.Integer('Color Index', default=0, help="Couleur de l'étape")
