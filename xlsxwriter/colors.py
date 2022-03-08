import xlsxwriter
from pathlib import Path


if __name__ == "__main__":
    path_xlsx = Path("trash.xlsx")
    workbook = xlsxwriter.Workbook(path_xlsx)
    worksheets = []
    worksheets.append(workbook.add_worksheet("pagina_0"))
    bg_gray = workbook.add_format({"bg_color": "gray"})
    my_bg_gray = workbook.add_format({"bg_color": "#c0c0c0"})  # dark 25%, 256 * 25% = 192, i.e. 0xc0
    font_green_bold = workbook.add_format({
        "font_color": "green",
        "bold": True,
    })
    my_font_green_bold = workbook.add_format({
        "font_color": "#00aa00",
        "bold": True,
    })
    worksheets[0].write(0, 0, "Alfredo", bg_gray)
    worksheets[0].write(0, 1, "Aurelien", my_bg_gray)
    worksheets[0].write(1, 0, "Caziani", font_green_bold)
    worksheets[0].write(1, 1, "Geron", my_font_green_bold)

    # Q: incremental, ok?
    # A: No, the latter will overwrite the former.
    font_bold = workbook.add_format({
        "bold": True,
    })
    worksheets[0].write(0, 2, "", my_bg_gray)
    worksheets[0].write(0, 2, "Ari", font_bold)
    worksheets[0].write(1, 2, "Seff")

    workbook.close()
