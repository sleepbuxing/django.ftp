from datetime import date, datetime, timedelta

def isholiday(nianyueri):
    holiday = ['20190913', '20191001', '20191002', '20191003', '20191004', '20191007']
    num = -1
    flag = 1
    #yesterday = (date.today() + timedelta(num)).strftime('%Y%m%d')
    #yesterday = (date.today() + timedelta(num))
    yesterday = datetime.strftime(nianyueri, "%Y%m%d")


    while flag:
        if yesterday in holiday:
            num -= 1
            #yesterday = (date.today() + timedelta(num)).strftime('%Y%m%d')
            #yesterday = (date.today() + timedelta(num))
            yesterday = datetime.strptime(yesterday, "%Y%m%d")
            yesterday = (nianyueri + timedelta(num))
            yesterday = datetime.strftime(yesterday, "%Y%m%d")
        else:
            flag = 0
    yesterday = datetime.strptime(yesterday, "%Y%m%d")
    return yesterday


#判断给定的日期是周几，周一到周日是0-6
def isweekend():
    week = (date.today() + timedelta(-1)).weekday()
    if week in [5, 6]:
        weekfre = (date.today() + timedelta(-2)).weekday()
        if weekfre in [5, 6]:
            weekfrefre = (date.today() + timedelta(-3)).weekday()
            #print(weekfrefre)
            #nianyueri = (date.today() + timedelta(-3)).strftime('%Y%m%d')
            nianyueri = (date.today() + timedelta(-3))
            nianyueri = isholiday(nianyueri)
            return nianyueri
        else:
            nianyueri = (date.today() + timedelta(-2))
            nianyueri = isholiday(nianyueri)
            return nianyueri
    else:
        nianyueri = (date.today() + timedelta(-1))
        nianyueri = isholiday(nianyueri)
    return nianyueri


