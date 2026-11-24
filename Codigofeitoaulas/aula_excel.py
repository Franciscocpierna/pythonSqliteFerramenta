import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Dados"
ws["A1"] = "Produto"
ws["B1"] = "Valor"
ws.append(["Teclado", 150])

wb.save("teste_excel.xlsx")
print("Planilha criada com sucesso!")