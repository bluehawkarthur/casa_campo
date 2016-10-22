#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min
import decimal
from apps.compras.models import Compras


def WriteToCompras(weather_data, fecha_de, fecha_a, total, town=None):
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

    title_text = u"{0}".format(ugettext("REPORTE DE COMPRAS"))
    title_empresa = u"{0}".format(ugettext("CASA DE CAMPO"))
    # merge cells
    worksheet_s.merge_range('D2:F2', title_text, title)
    worksheet_s.merge_range('A2:C2', title_empresa, cell2)


    # write header

    fechas = '%s %s %s %s' % ('De:', fecha_de, 'A:', fecha_a)
    worksheet_s.merge_range('A4:D4', ugettext(fechas), cell2)


    # worksheet_s.write(3, 0, ugettext("Nombre o Razon Social:"), cell)
    # worksheet_s.write(3, 1, ugettext(mes), cell)
    # format = workbook.add_format()
    header.set_text_wrap()

    worksheet_s.write(6, 0, ugettext("Cod."), header)
    worksheet_s.write(6, 1, ugettext("Descripcion"), header)
    worksheet_s.write(6, 2, ugettext("Unidad"), header)
    worksheet_s.write(6, 3, ugettext("Cantidad"), header)
    worksheet_s.write(6, 4, ugettext("Pr. Unid"), header)
    worksheet_s.write(6, 5, ugettext("Total"), header)
    worksheet_s.write(6, 6, ugettext("Comprob,"), header)
    worksheet_s.write(6, 7, ugettext("Fecha"), header)
    worksheet_s.write(6, 8, ugettext("Fact."), header)
    


    totales = 0
    b = 0
    tc = 0
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 7 + idx
        # neto = data.total - data.ice - data.excentos
        # importe_base = neto - data.descuento
       

        if data['cantidad'] or data['pr_costo']:
            cant = data['cantidad']
            pr = data['pr_costo']
        else:
            cant = 0
            pr = 0

        total_compra = cant*pr
        totales = totales + total_compra

        if data['fecha']:
            fc = data['fecha'].strftime('%d/%m/%Y')
        else:
            fc = ''

        worksheet_s.write_string(row, 0, data['codigo'], cell)
        worksheet_s.write_string(row, 1, data['descripcion'], cell)
        worksheet_s.write_string(row, 2, data['unidad'], cell)

        if data['cantidad']:
            worksheet_s.write_number(row, 3, data['cantidad'], cell_center)
        else:
            worksheet_s.write_string(row, 3, '', cell_center)

        if data['pr_costo']:
            worksheet_s.write_number(row, 4, data['pr_costo'], cell_center)
        else:
            worksheet_s.write_string(row, 4, '', cell_center)

        worksheet_s.write_number(row, 5, data['total_compra'], cell_center)
        worksheet_s.write_string(row, 6, data['comprobantetxt'], cell_center)
        worksheet_s.write_string(row, 7, fc, cell_center)
        if data['factura']:
            worksheet_s.write_number(row, 8, data['factura'], cell_center)
        else:
            worksheet_s.write_string(row, 8, '', cell_center)

        # if b == 0:
        #     b = data.compras.comprobante

        # if b == data.compras.comprobante:
        #     worksheet_s.write_string(row, 0, data.codigo, cell)
        #     worksheet_s.write_string(row, 1, data.descripcion, cell)
        #     worksheet_s.write_string(row, 2, data.unidad, cell)
        #     worksheet_s.write_number(row, 3, data.cantidad, cell_center)
        #     worksheet_s.write_number(row, 4, data.pr_costo, cell_center)
        #     worksheet_s.write_number(row, 5, total_compra, cell_center)
        #     worksheet_s.write_string(row, 6, data.compras.comprobantetxt, cell_center)
        #     worksheet_s.write_string(row, 7, data.compras.fecha.strftime('%d/%m/%Y'), cell_center)
        #     worksheet_s.write_number(row, 8, data.compras.factura, cell_center)
        #     tc = tc + total_compra

        # else:
          
        #     worksheet_s.write_string(row, 0, '', cell)
        #     worksheet_s.write_string(row, 1, 'Total Comp.', cell)
        #     worksheet_s.write_string(row, 2, '', cell)
        #     worksheet_s.write_string(row, 3, '', cell)
        #     worksheet_s.write_string(row, 4, '', cell_center)
        #     worksheet_s.write_number(row, 5, tc, cell_center)
        #     worksheet_s.write_string(row, 6, '-------', cell_center)
        #     worksheet_s.write_string(row, 7, '', cell_center)
        #     worksheet_s.write_string(row, 8, '', cell_center)
            
        #     b = 0
        #     tc = 0


    # change column widths
    worksheet_s.set_column('B:B', 25)  # Town column
    worksheet_s.set_row(6, 30)
    worksheet_s.set_column('C:C', 11)  # Date column
    worksheet_s.set_column('D:D', 12)  # Description column
    worksheet_s.set_column('E:E', 12)  # Max Temp column
    worksheet_s.set_column('F:F', 15)  # Min Temp column
    worksheet_s.set_column('G:G', 15)  # Wind Speed column
    worksheet_s.set_column('H:H', 11)  # Precipitation column
    worksheet_s.set_column('I:I', 11)  # Precipitation % column
    worksheet_s.set_column('J:J', 10)  # Observations column
    worksheet_s.set_column('L:L', 12)

    row = row + 1
  
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    worksheet_s.write(row, 5, totales, cell_total)
    

    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

