




## Multiple Formats in The Same Cell
Use `write_rich_string()`. E.g.
```python
bold   = workbook.add_format({'bold': True})
italic = workbook.add_format({'italic': True})

worksheet.write_rich_string('A1',
                            'This is ',
                            bold, 'bold',
                            ' and this is ',
                            italic, 'italic')
```

For more info, cf. <https://xlsxwriter.readthedocs.io/worksheet.html#worksheet-write-rich-string>



