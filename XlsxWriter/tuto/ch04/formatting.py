import xlsxwriter

workbook = xlsxwriter.Workbook("Expenses02.xlsx")
worksheet = workbook.add_worksheet()

# formats are to be put in write() as the third arg,
# right after the position arg (1st arg) and the content arg (2nd arg)
bold = workbook.add_format({"bold": True})
money = workbook.add_format({"num_format": "$#,##0"})

# header
worksheet.write("A1", "Item", bold)
worksheet.write("B1", "Cost", bold)

# data
expenses = (
    ["Rent", 1000],
    ["Gas",   100],
    ["Food",  300],
    ["Gym",   50],
)

# row-0 has reserved to the header
row = 1

for item, cost in expenses:
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, cost, money)
    row += 1

# summary
worksheet.write(row, 0, "Total", bold)
worksheet.write(row, 1, "=SUM(B2:B5)", money)

workbook.close()
