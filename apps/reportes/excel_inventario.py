#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min
import decimal
from apps.compras.models import Compras


def WriteToInventario(weather_data, inventario, fecha, total, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Libro de Compras")

    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })

    title2 = workbook.add_format({
        'bold': True,
        'font_size': 12,
        'align': 'center',
        'valign': 'vcenter'
    })

    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell2 = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'bold': True
    })

    cell_total = workbook.add_format({
        'bold': True,
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell_center = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    cell_center2 = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'bold': True
    })

    # write title
    if town:
        town_text = town.name
    else:
        town_text = ugettext("all recorded towns")

    title_text = u"{0}".format(ugettext("INVENTARIO FISICO"))
    if inventario == 'valorado':
        title_text = title_text = u"{0}".format(ugettext("INVENTARIO VALORADO"))

    title_empresa = u"{0}".format(ugettext("CASA DE CAMPO"))
    # merge cells
    worksheet_s.merge_range('C2:E2', title_text, title)
    worksheet_s.merge_range('A2:B2', title_empresa, cell2)
    worksheet_s.merge_range('F2:G2', fecha, title)


    worksheet_s.write(5, 0, ugettext("Cod."), header)
    worksheet_s.write(5, 1, ugettext("Descripcion"), header)
    worksheet_s.write(5, 2, ugettext("Unidad"), header)
    worksheet_s.write(5, 3, ugettext("Cantidad"), header)

    if inventario == 'valorado':
        worksheet_s.write(5, 4, ugettext("Pr. Unid"), header)
        worksheet_s.write(5, 5, ugettext("Total"), header)

    totales = 0
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 6 + idx
        totales = totales + data['total']

        worksheet_s.write_string(row, 0, data['codigo'], cell)
        worksheet_s.write_string(row, 1, data['descripcion'], cell)
        worksheet_s.write_string(row, 2, data['unidad'], cell)
        worksheet_s.write_number(row, 3, data['cantidad'], cell_center)
        if inventario == 'valorado':
            worksheet_s.write_number(row, 4, data['pr_costo'], cell_center)
            worksheet_s.write_number(row, 5, data['total'], cell_center)

    # change column widths
    worksheet_s.set_column('B:B', 25)  # Town column
    worksheet_s.set_column('A:A', 20)
    worksheet_s.set_row(5, 30)
    worksheet_s.set_column('C:C', 15)  # Date column
    worksheet_s.set_column('D:D', 15)  # Description column
    worksheet_s.set_column('E:E', 15)  # Max Temp column
    worksheet_s.set_column('F:F', 15)  # Min Temp column
    worksheet_s.set_column('G:G', 15)  # Wind Speed column
    worksheet_s.set_column('H:H', 11)  # Precipitation column
    worksheet_s.set_column('I:I', 11)  # Precipitation % column
    worksheet_s.set_column('J:J', 10)  # Observations column
    worksheet_s.set_column('L:L', 12)

    row = row + 1

    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    if inventario == 'valorado':
        worksheet_s.write(row, 5, totales, cell_total)


    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

