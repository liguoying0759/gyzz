# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class test1(models.Model):
#     _name = 'test1.test1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class MyPartner(models.Model):
    _name = 'test1.test1'

    name = fields.Char(string='name')
    haha = fields.Char(string='haha')
    start_date = fields.Datetime(string='开始时间')
    end_date = fields.Datetime(string='结束时间')
    duration = fields.Float(string='持续时间')
    color = fields.Integer()