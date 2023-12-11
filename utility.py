from datetime import datetime, timedelta
from pytz import timezone 

def compareDate_wrt_currentTime(given_date):
    given_date = datetime.strptime(given_date, "%a, %d %b %Y %H:%M:%S %z")
    # print(type(given_date),"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",given_date)
    currTime = datetime.now(timezone("Asia/Kolkata"))-timedelta(days=2)
    # currTime = currTime.strftime("%Y-%m-%d %H:%M:%S.%f%z")
    # print(type(currTime),"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",currTime)
    print(currTime)
    print(given_date)
    if given_date >= currTime:
        return True
    return False




a = datetime.now(timezone("Asia/Kolkata"))-timedelta(minutes=19)
# print(compareDate_wrt_currentTime(a))
