from datetime import datetime
import pytz

def timezones():
    citys = ["America/Argentina/Buenos_Aires","America/New_York America/Mexico_City","America/Mexico_City"]

    for city in citys:
        city_timezone = pytz.timezone(city)

        city_date = datetime.now(city_timezone)
        print(f"City of {city}: ", city_date.strftime("%d/%m/%Y, %H:%M:%S"))


def run():
    timezones()

if __name__=="__main__":
    run()