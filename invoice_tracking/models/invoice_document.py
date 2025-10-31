from odoo import models, fields, api

class InvoiceDocument(models.Model):
    _name = 'invoice.document'
    _description = 'Invoice Document'

    name = fields.Char("Document Name", required=True)
    required = fields.Boolean("Required?", default=True)
    file = fields.Binary("Document File")
    document_id = fields.Many2one("documents.document", "Related Document")

