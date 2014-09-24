from xlrd import open_workbook

book = open_workbook('blog_data.xls')

sheet = book.sheet_by_index(0)

column_names = [c.value for c in sheet.row(0)]

for row_index in range(1, sheet.nrows):
	row = sheet.row(row_index)
	for (column_index, column_name) in enumerate(column_names):
		print column_name, ':', row[column_index].value.encode('ascii', 'replace')
