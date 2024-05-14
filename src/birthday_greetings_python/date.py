import datetime


class Date:
    def __init__(self, str_date: str):
        year, month, day = [int(x) for x in str_date.split("/")]
        self.date = datetime.date(year, month, day)

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        return self.date.strftime("%Y/%m/%d")

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month

    @property
    def day(self):
        return self.date.day
