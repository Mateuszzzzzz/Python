from datetime import datetime

date_string = "Dec 14 2022 4:20PM"

datetime_real = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

print(datetime_real)
