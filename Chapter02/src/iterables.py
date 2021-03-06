"""iterables"""
from datetime import timedelta, date


class DateRangeIterable:
    """ An iterable"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateContainerIterable:
    """ An iterable"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_date = self.start_date
        while current_date < self.end_date:
            yield current_date
            current_date += timedelta(days=1)


class DateRangeSequence:
    """An range created by wrapping a sequence."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


if __name__ == "__main__":
    for day in DateRangeIterable(date(2022, 1, 1), date(2022, 1, 10)):
        print(day)