from openpyxl import load_workbook


# read excel file from bytes
def read_excel(file):
    wb = load_workbook(filename=file, read_only=True)
    ws = wb.active
    data = []
    for row in ws.rows:
        data.append([cell.value for cell in row])
    return data[1:]
