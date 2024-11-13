from datetime import date, timedelta

def get_Date():
    yesterday = date.today() - timedelta(days=1)
    date_string = yesterday.strftime('%Y%m%d')
    date_string_dash = yesterday.strftime('%Y-%m-%d')
    print('Info called date_string_dash: ',  date_string_dash)
    return date_string_dash
