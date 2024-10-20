from odoo import api, models, fields
from odoo.http import request

class ProjectManagement(models.Model):
    _name = 'project.management'
    _description = 'model for project management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    status = fields.Selection(
        [
            ('planning', 'Planning'),
            ('in_progress', 'In Progress'),
            ('on_hold', 'On Hold'),
            ('completed', 'Completed'),
        ],
        default='planning'
    )
    assigned_team = fields.Many2many('hr.employee')
    tasks_ids = fields.One2many('project.task', 'project_id')

    def action_generate_excel_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/project_management/report/excel/{self.env.context.get("active_ids")}',
            'target': 'new'
        }

    @api.model
    def get_project_statistics(self):
        projects = self.search([])
        total_projects = len(projects)
        completed_projects = sum(project.status == 'completed' for project in projects)
        overall_completion = (completed_projects / total_projects) * 100 if total_projects else 0

        upcoming_deadlines = projects.filtered(lambda p: p.end_date and p.end_date > fields.Date.today()).sorted('end_date')

        deadlines = [{'name': project.name, 'date': project.end_date} for project in upcoming_deadlines]

        return {
            'completion': overall_completion,
            'deadlines': deadlines,
        }
