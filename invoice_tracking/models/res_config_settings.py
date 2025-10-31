# -*- coding: utf-8 -*-
from odoo import models, fields, api, Command

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_clearance_date = fields.Integer("Number of day for clearance", required=True, readonly=False,
                                            related="company_id.clearance_date", default_model='res.company')

    invoice_document_folder = fields.Many2one("documents.document", "Default Document Folder", required=True, readonly=False,
                                              domain="[('type', '=', 'folder')]", related="company_id.invoice_document_folder",
                                              default_model='res.company')
