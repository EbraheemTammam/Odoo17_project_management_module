from odoo import models, fields

class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'model for project task'

    name = fields.Char(required=True)
    project_id = fields.Many2one('project.management', ondelete="cascade")
    description = fields.Text()
    assigned_to = fields.Many2one('hr.employee')
    priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        default='medium'
    )
    status = fields.Selection(
        [
            ('to_do', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ],
        default='to_do'
    )
