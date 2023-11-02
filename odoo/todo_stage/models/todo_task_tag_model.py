# noinspection PyUnresolvedReferences
from odoo import models, fields


class Tag(models.Model):
    _name = 'todo_stage.tag'
    _description = 'To-do Tag'

    name = fields.Char('Name', translate=True)
