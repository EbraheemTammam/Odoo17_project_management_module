from ast import literal_eval
from odoo import http
from odoo.http import request
import io
import xlsxwriter

class ProjectManagementXLSXReport(http.Controller):

    @http.route('/project_management/report/excel/<string:project_ids>', type='http', auth='user')
    def get_excel_report(self, project_ids):
        project_ids = request.env['project.management'].browse(literal_eval(project_ids))
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("Project Performance Report")
        header_format = workbook.add_format({'bold': True, 'bg_color': '#5bc0de', 'color': '#ffffff', 'border': 1, 'align': 'center'})
        text_format = workbook.add_format({'text_wrap': True, 'align': 'center'})
        headers = ['Project Name', 'Description', 'Status', 'Start Date', 'End Date', 'Task Name', 'Status', 'Assigned To', 'Priority']
        for i, header in enumerate(headers):
            worksheet.write(0, i, header, header_format)
        row = 1
        for project in project_ids:
            worksheet.write(row, 0, project.name, text_format)
            worksheet.write(row, 1, project.description, text_format)
            worksheet.write(row, 2, project.status, text_format)
            worksheet.write(row, 3, str(project.start_date), text_format)
            worksheet.write(row, 4, str(project.end_date), text_format)
            for task in project.tasks_ids:
                worksheet.write(task.id + row, 5, task.name, text_format)
                worksheet.write(task.id + row, 6, task.status, text_format)
                worksheet.write(task.id + row, 7, task.assigned_to.name, text_format)
                worksheet.write(task.id + row, 8, task.priority, text_format)
            row += 1
        workbook.close()
        output.seek(0)
        file_name = "ProjectPerformance.xlsx"
        return request.make_response(
            output.getvalue(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=%s;' % file_name)
            ]
        )
