from odoo import models


class ProfInformationXLSX(models.AbstractModel):
    _name = 'report.module_test.report_prof_information_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines", lines, data)
        format1 = workbook.add_format({'font_size': 12, 'align':'vcenter', 'bold':True})
        format2 = workbook.add_format({'font_size': 9, 'align':'vcenter',})
        sheet = workbook.add_worksheet('Prof Information')
        sheet.write(0,0,'Name',format1)
        sheet.write(0,1,'Course',format1)
        sheet.write(0,2,'Age',format1)
        sheet.write(0,3,'Salary',format1)
        sheet.write(0,4,'Gender',format1)
        sheet.write(0,5,'ladder',format1)

        sheet.write(1,0,lines.name,format2)
        sheet.write(1,1,lines.course.name,format2)
        sheet.write(1,2,lines.age,format2)
        sheet.write(1,3,lines.salary,format2)
        sheet.write(1,4,lines.gender,format2)
        sheet.write(1,5,lines.ladder,format2)