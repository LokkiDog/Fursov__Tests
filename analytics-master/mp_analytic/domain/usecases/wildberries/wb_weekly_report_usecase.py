import datetime

from config.color_constants import *
from data.google.get_body_methods.get_body import *
from data.google.get_range_methods.get_range import get_range_colorize
from data.google.sheet.sheet_api import GoogleSheetAPI
from data.repository.wildberries.wb_weekly_report import WeeklyReport
from data.utils.functions import update_at
from domain.utils.wb_drf_data_weekly_monthly import get_drf_data


class WeeklyReportUseCase:
    """
    Ежедневный отчет за неделю
    """

    def __init__(self, kwargs: dict):
        self.kwargs = kwargs

        self.update_at = None
        self.dashboard_data = None

    def execute(self):
        suppliers = self.kwargs.get("suppliers")
        spreadsheet_id = self.kwargs.get("Wildberries")

        sheet_title_plan = "План"
        sheet_id_plan = self.kwargs.get(sheet_title_plan)

        row = GoogleSheetAPI(sheet_title_plan, spreadsheet_id, sheet_id_plan).get_row(1)[0]

        sheet_title = "Неделя"
        sheet_id = self.kwargs.get(sheet_title)

        table = GoogleSheetAPI(sheet_title, spreadsheet_id, sheet_id)

        plan = [int(i) for i in row]
        report = WeeklyReport(datetime.datetime.today().isoweekday() - 1, suppliers)
        response = report.execute(plan)
        table.clear()
        table.insert(response)
        self.clear_color(table)
        self.design_table(table)

        self.update_at = update_at(response)

        self.dashboard_data = get_drf_data(response)

        return self.update_at

    def design_table(self, table):
        _range = get_range_colorize
        _body = get_body_colorize
        body = {"requests": []}
        _body(body, _range(0, 1, 0, 8, table.sheet_id), BLUE_LIGHT)
        _body(body, _range(8, 9, 0, 8, table.sheet_id), BLUE_LIGHT)

        table.conditional_color_format(10, 11)

        _body(body, _range(12, 13, 0, 8, table.sheet_id), SKIN_LIGHT)
        _body(body, _range(13, 14, 0, 8, table.sheet_id), PURPLE_LIGHT)
        _body(body, _range(14, 15, 0, 8, table.sheet_id), PINK_LIGHT)
        _body(body, _range(15, 16, 0, 8, table.sheet_id), PURPLE_LIGHT)
        _body(body, _range(16, 17, 0, 8, table.sheet_id), SKIN)
        _body(body, _range(17, 18, 0, 8, table.sheet_id), SKIN_LIGHT)
        _body(body, _range(18, 19, 0, 8, table.sheet_id), SALAD)
        _body(body, _range(19, 20, 0, 8, table.sheet_id), SKIN_SUPER_LIGHT)

        table.colorize_row(body)

        table.number_format(1, 10, 1, 7)
        table.number_format(12, 15, 1, 7)
        table.number_format(17, 19, 1, 7)

        table.percent_format(1, 19, 7, 8)
        table.percent_format(10, 12, 1, 8)
        table.percent_format(15, 17, 1, 8)
        table.percent_format(19, 20, 1, 8)

    def clear_color(self, table):
        table.colorize_row()
