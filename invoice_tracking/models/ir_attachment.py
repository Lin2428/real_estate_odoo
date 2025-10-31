# -*- coding: utf-8 -*-

from odoo import models, api


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        attachment = super(IrAttachment, self).create(vals)
        attachment.create_from_attachment()
        return attachment

    def create_from_attachment(self):
        if self.res_model == 'invoice.tracking':
            # Recherche ou création du dossier "Invoice Tracking"
            link = self.env['documents.folder'].search([('name', '=', 'Invoice Tracking')], limit=1)
            if not link:
                link = self.env['documents.folder'].create({
                    'name': 'Invoice Tracking',
                    'company_id': (self.company_id or self.env.company).id,
                })

            # Vérifie si le document existe déjà
            if not self.env['documents.document'].search([
                ('attachment_id', '=', self.id),
                ('folder_id', '=', link.id)
            ]):
                model = self.env.get(self.res_model)
                model_res = model.browse(self.res_id)
                partner = model_res.partner_id if hasattr(model_res, 'partner_id') else False

                self.env['documents.document'].create({
                    'attachment_id': self.id,
                    'name': self.name,
                    'folder_id': link.id,
                    'owner_id': self.create_uid.id,
                    'partner_id': partner.id if partner else False
                })