from config.sheets import SHEETS, SPREADSHEET_ID_SECOND
from data.google.sheet.sheet_api import GoogleSheetAPI
from data.repository.wildberries.wb_report_sell_percent_by_article import SellPercentReportByArticle


class SellPercentReportByArticleUseCase:
    """
    Отчет "Процент выкупа (Артикул)"
    """

    def execute(self) -> str:
        response = SellPercentReportByArticle().execute()

        sheet_title = SHEETS.get('percent_article').get('title')
        sheet_id = SHEETS.get('percent_article').get('id')

        table = GoogleSheetAPI(sheet_title, SPREADSHEET_ID_SECOND, sheet_id)

        table.clear()
        table.insert(response)

        return table.get_sheet_url()
