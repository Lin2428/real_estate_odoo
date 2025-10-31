# -*- coding: utf-8 -*-
from odoo import models, fields, api, Command

class ResCompany(models.Model):
    _inherit = 'res.company'

    clearance_date = fields.Integer("Number of day for clearance",required=True, default=15)
    invoice_document_folder = fields.Many2one("documents.document", "Default Document Folder", required=True,
                                              domain="[('type', '=', 'folder')]")
