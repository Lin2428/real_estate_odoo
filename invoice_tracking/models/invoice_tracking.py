from odoo import models, fields, api,_

class InvoiceTracking(models.Model):
    _name = "invoice.tracking"
    _description = "Invoice Tracking"
    _inherit = [
        'mail.thread.cc',
        'mail.activity.mixin',
    ]

    def _get_default_stage_id(self):
        """ return default stage_id """
        default_stage = self.env['invoice.stage'].search([], order='sequence', limit=1)
        if not default_stage:
            return False
        return default_stage.id

    name = fields.Char("Protocol Number", required=True, default=lambda self: _('New'))
    invoice_number = fields.Char("Number", required=True)
    description = fields.Html("Description")
    stage_id = fields.Many2one("invoice.stage", "Stage", default=_get_default_stage_id, required=True)
    invoice_documents_ids = fields.Many2many("ir.attachment", compute="_get_documents")
    partner_id = fields.Many2one('res.partner', string='Partner')
    amount = fields.Monetary("Invoice amount", currency_field='company_currency_id')
    company_currency_id = fields.Many2one('res.currency', string='Currency',
                                          default=lambda self: self.env.company.currency_id)
    invoice_date = fields.Date("Invoice date")
    reception_date = fields.Date("Reception date")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('invoice.tracking') or _('New')
        return super(InvoiceTracking, self).create(vals)

    def _get_documents(self):
        for invoice in self:
            invoice.invoice_documents_ids = self.env['ir.attachment'].search(
                [('res_id', '=', invoice.id), ('res_model', '=', 'invoice.tracking')]).ids

    def action_add_document(self):
        self.ensure_one()
        return {
            'name': 'Create Attachment',
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'view_mode': 'form',
            'view_id': self.env.ref('h4s_purchase_wholesale.view_attachment_form').id,
            'context': {'default_res_model': self._name, 'default_res_id': self.id},
            'target': 'new',
        }