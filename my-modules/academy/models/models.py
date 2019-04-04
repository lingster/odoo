# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = "Academy teachers"

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string='Courses')
    #course_ids = fields.One2many('product.template', 'teacher_id', string='Courses')


class Courses(models.Model):
    _name = 'academy.courses'
    #_inherit = 'product.template'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")


class Academy(models.Model):
    _name = 'academy.academy'
    _description = 'Academy Academy description'

    name = fields.Char()
    value = fields.Integer()
    value_pct = fields.Float(compute="_value_pct", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pct(self):
        self.value_pct = float(self.value) / 100


class Course(models.Model):
    _name = 'academy.course'
    _description = "Academy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class Session(models.Model):
    _name = 'academy.session'
    _description = 'Academy Sessions'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="duration in days")
    seats = fields.Integer(string="Number of seats")
