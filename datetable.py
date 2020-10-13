import datetime as _datetime
import pandas as _pandas
import sys
from dateutil.parser import parse
from pandas.tseries.offsets import BDay

def _create_date_table(date=None, date_format=None):
    """
    Create a date table with all its attributes
    """


    if date is None:
        _date_range =  _pandas.date_range('1990-04-07',_datetime.datetime.now())
    else:
        try:
            _date = parse(date)
            _date_range = _pandas.date_range(_date, _datetime.datetime.now())
        except ValueError:
            if not date_format is None:
                try:
                    _date = _datetime.strptime(date, date_format)
                    _date_range = _pandas.date_range(_date, _datetime.datetime.now())
                except ValueError:
                    raise ValueError('The specified date format is not valid')

    datetable = _pandas.DataFrame(_date_range, columns=['date'], dtype='datetime64[ns]')
    datetable['year'] = datetable.date.dt.year
    datetable['month'] = datetable.date.dt.month
    datetable['month_pad'] = datetable.month.map('{:02}'.format)
    datetable['month_name'] = datetable.date.dt.month_name()
    datetable['year_month'] = datetable.date.dt.to_period(freq='M')
    datetable['month_start'] = datetable.date.dt.floor('d') - _pandas.offsets.MonthBegin(1)
    datetable['month_end'] = datetable.date.dt.floor('d') - _pandas.offsets.MonthEnd(1)
    datetable['day'] = datetable.date.dt.day
    datetable['day_pad'] = datetable.day.map('{:02}'.format)
    datetable['day_of_week'] = datetable.date.dt.weekday
    datetable['day_of_year'] = datetable.date.dt.dayofyear
    datetable['day_name'] = datetable.date.dt.day_name()
    datetable['ordinal_week'] = datetable.date.dt.isocalendar().week
    datetable['hour'] = datetable.date.dt.hour
    datetable['minute'] = datetable.date.dt.minute
    datetable['second'] = datetable.date.dt.second
    datetable['quarter'] = datetable.date.dt.quarter
    datetable['business_day'] = datetable.date.apply(lambda x: x + BDay(1))

    return datetable


class DateTable:
    """
    <summary>
    """

    def __new__(cls, dataframe=None):
        cls.dataframe = dataframe
    

    @classmethod
    def table(cls, date=None, date_format=None):
        """
        This function return the date table

        date: should be a valid date format , default is '1990-04-07' %Y-%m-%d
        format: The format in which the date is, if the date is in a special format that dateutil.parser.parse can't identify
        """
        return _create_date_table(date, date_format)

_pandas.options.display.max_columns = 200
print(DateTable.table())