# -*- coding: utf-8 -*-

from odoo import models, fields

# class module_test(models.Model):
#     _name = 'module_test.module_test'
#     _description = 'module_test.module_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'My Course'

    name = fields.Char(string='Name', required=True, help='Name of the Course', translate=True)
    description = fields.Text(translate=True)
    responsible_id = fields.Many2one('res.users',ondelete='set null', string="Responsible", index=True)


class Student(models.Model):
    _name = 'openacademy.student'
    _description = 'Student Information'

    name = fields.Char(string='Name Student', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')


class Prof(models.Model):
    _name = 'openacademy.prof'
    _description = 'Professeur Information'

    name = fields.Char(string='Name Professeur', required=True)
    course = fields.Many2one('openacademy.course', string='Course name', required=True)
    age = fields.Integer(string='Age Professeur', required=True)
    salary = fields.Integer(string='Salary', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    ladder = fields.Selection([
        ('PES', 'PES'),
        ('PA', 'PA'),
        ('PH', 'PH'),
    ], string='ladder', default='PA')
    image = fields.Image(string='Image Prof')


class Sessions(models.Model):
    _name = 'openacademy.sessions'
    _description = 'Sessions Helpdesk'
    _rec_name = 'user_name'

    def action_en_cours(self):
        for rec in self:
            rec.state = 'session en cours'

    def action_finished(self):
        for rec in self:
            rec.state = 'session finished'

    user_name = fields.Char(string='le nom de la session', required=True)
    password = fields.Char(string='password', required=True)
    notes = fields.Char(string='Notes', help='cite what you have about the session')
    prof = fields.Many2many('openacademy.prof',  string='Prof Name', required=True)
    state = fields.Selection([
        ('session started', 'Session Started'),
        ('session en cours', 'Session En Cours'),
        ('session finished', 'Session Finished')
    ], string='Status', index=True, readonly=True, default='session started')
