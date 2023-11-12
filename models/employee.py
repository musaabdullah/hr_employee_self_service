# # -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

# class HrEmployee(models.Model):
#     _inherit = 'hr.employee'
    
#     # @api.multi
#     def write(self, vals):
#         rec = super(HrEmployee, self).write(vals)
#         self.ensure_one()
# #         uid = self._context.get('uid')
# #         group = self.env['res.groups'].search([('name', '=', 'Employee')])
# #         categ_id = group.category_id.id
# #         officer_group = self.env['res.groups'].search([('name','=','Officer'),('category_id','=',categ_id)])
#         user_id = self.env['res.users'].browse(self._context.get('uid'))

#         if user_id.has_group('hr.group_hr_user'):
#             return rec

#         if user_id.has_group('base.group_user'):
#             if self.user_id == user_id:
#                 return rec
#             else:
#                 raise UserError(_('You have no rights for update other employees data.'))
