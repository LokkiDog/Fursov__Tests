expected_add_sheet = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'replies': [{'addSheet': {'properties': {'sheetId': 854162543, 'title': 'sheet_title', 'index': 3, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}}]}
expected_add_sheet_exceptions = {'replies': [{'addSheet': {'properties': {'gridProperties': {'columnCount': 26, 'rowCount': 1000}, 'index': 3, 'sheetId': 854162543, 'sheetType': 'GRID', 'title': 'sheet_title'}}}], 'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo'}

expected_get_all = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'properties': {'title': 'Tests', 'locale': 'ru_RU', 'autoRecalc': 'ON_CHANGE', 'timeZone': 'Europe/Moscow', 'defaultFormat': {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 'verticalAlignment': 'BOTTOM', 'wrapStrategy': 'OVERFLOW_CELL', 'textFormat': {'foregroundColor': {}, 'fontFamily': 'arial,sans,sans-serif', 'fontSize': 10, 'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'foregroundColorStyle': {'rgbColor': {}}}, 'backgroundColorStyle': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, 'spreadsheetTheme': {'primaryFontFamily': 'Arial', 'themeColors': [{'colorType': 'TEXT', 'color': {'rgbColor': {}}}, {'colorType': 'BACKGROUND', 'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, {'colorType': 'ACCENT1', 'color': {'rgbColor': {'red': 0.25882354, 'green': 0.52156866, 'blue': 0.95686275}}}, {'colorType': 'ACCENT2', 'color': {'rgbColor': {'red': 0.91764706, 'green': 0.2627451, 'blue': 0.20784314}}}, {'colorType': 'ACCENT3', 'color': {'rgbColor': {'red': 0.9843137, 'green': 0.7372549, 'blue': 0.015686275}}}, {'colorType': 'ACCENT4', 'color': {'rgbColor': {'red': 0.20392157, 'green': 0.65882355, 'blue': 0.3254902}}}, {'colorType': 'ACCENT5', 'color': {'rgbColor': {'red': 1, 'green': 0.42745098, 'blue': 0.003921569}}}, {'colorType': 'ACCENT6', 'color': {'rgbColor': {'red': 0.27450982, 'green': 0.7411765, 'blue': 0.7764706}}}, {'colorType': 'LINK', 'color': {'rgbColor': {'red': 0.06666667, 'green': 0.33333334, 'blue': 0.8}}}]}}, 'sheets': [{'properties': {'sheetId': 0, 'title': 'Лист1', 'index': 0, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}, {'properties': {'sheetId': 195541656, 'title': 'Лист2', 'index': 1, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}, {'properties': {'sheetId': 1427492153, 'title': 'Лист3', 'index': 2, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}, {'properties': {'sheetId': 1144711631, 'title': 'sheet_title', 'index': 3, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}], 'spreadsheetUrl': 'https://docs.google.com/spreadsheets/d/12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo/edit'}

expected_spreadsheet_create = {'spreadsheetId': '1gvFpgZnWE79mX5C2GtQ1hEUIukmJjRY9T7jko9W9EOE', 'properties': {'title': 'New', 'locale': 'ru_RU', 'autoRecalc': 'ON_CHANGE', 'timeZone': 'Etc/GMT', 'defaultFormat': {'backgroundColor': {'red': 1, 'green': 1, 'blue': 1}, 'padding': {'top': 2, 'right': 3, 'bottom': 2, 'left': 3}, 'verticalAlignment': 'BOTTOM', 'wrapStrategy': 'OVERFLOW_CELL', 'textFormat': {'foregroundColor': {}, 'fontFamily': 'arial,sans,sans-serif', 'fontSize': 10, 'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'foregroundColorStyle': {'rgbColor': {}}}, 'backgroundColorStyle': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, 'spreadsheetTheme': {'primaryFontFamily': 'Arial', 'themeColors': [{'colorType': 'TEXT', 'color': {'rgbColor': {}}}, {'colorType': 'BACKGROUND', 'color': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}}, {'colorType': 'ACCENT1', 'color': {'rgbColor': {'red': 0.25882354, 'green': 0.52156866, 'blue': 0.95686275}}}, {'colorType': 'ACCENT2', 'color': {'rgbColor': {'red': 0.91764706, 'green': 0.2627451, 'blue': 0.20784314}}}, {'colorType': 'ACCENT3', 'color': {'rgbColor': {'red': 0.9843137, 'green': 0.7372549, 'blue': 0.015686275}}}, {'colorType': 'ACCENT4', 'color': {'rgbColor': {'red': 0.20392157, 'green': 0.65882355, 'blue': 0.3254902}}}, {'colorType': 'ACCENT5', 'color': {'rgbColor': {'red': 1, 'green': 0.42745098, 'blue': 0.003921569}}}, {'colorType': 'ACCENT6', 'color': {'rgbColor': {'red': 0.27450982, 'green': 0.7411765, 'blue': 0.7764706}}}, {'colorType': 'LINK', 'color': {'rgbColor': {'red': 0.06666667, 'green': 0.33333334, 'blue': 0.8}}}]}}, 'sheets': [{'properties': {'sheetId': 741948705, 'title': 'Title', 'index': 0, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}], 'spreadsheetUrl': 'https://docs.google.com/spreadsheets/d/1gvFpgZnWE79mX5C2GtQ1hEUIukmJjRY9T7jko9W9EOE/edit'}

expected_clear = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'clearedRange': 'sheet_title!A1:C2'}
expected_clear_no_title = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'clearedRange': 'Empty title!A1:C2'}


expected_get_column = [['1'], ['2', '3', '5'], ['4']]
expected_get_row = [['1', '2', '4'], ['', '3'], ['', '5']]

expected_insert = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'replies': [{'addSheet': {
        'properties': {'sheetId': 94459280, 'title': 'sheet_title', 'index': 3, 'sheetType': 'GRID',
        'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}}]}

expected_empty_reply = {'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo', 'replies': [{}]}

expected_batch_update = {'responses': [{'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo','updatedCells': 3,'updatedColumns': 1, 'updatedRange': 'sheet_title!A1:A3','updatedRows': 3}],'spreadsheetId': '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo','totalUpdatedCells': 3,'totalUpdatedColumns': 1,'totalUpdatedRows': 3,'totalUpdatedSheets': 1}