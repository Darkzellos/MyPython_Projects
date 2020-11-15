mode = input("Выберите режим: 1.Секунды в минуты, 2.Минуты в секунды, 3.Часы в минуты, 4.Часы в секунды:   ")
mode = int(mode)
def hours_in_seconds():
	hour = input(" Часов? ")
	hour = float(hour)
	minute = 60 * hour
	second = 60 * minute
	second = str(second)
	print("В секундах: " + second)
def hours_in_minute():
	hour = input(" Часов? ")
	hour = float(hour)
	minute = 60 * hour
	minute = str(minute)
	print("В минутах: " + minute)
def minute_in_seconds():
  minute = input(" Минут? ")
  minute = float(minute)
  second = 60 * minute
  second = str(second)
  print("В секундах: " + second)
def seconds_in_minute():
  second = input(" Секунд? ")
  second = float(second)
  minute = second / 60  
  minute = str(minute)
  print("В минутах: " + minute)
if mode == 1:
  seconds_in_minute()
elif mode == 2:
  minute_in_seconds()
elif mode == 3:
	hours_in_minute()
elif mode == 4:
	hours_in_seconds()
else:
  print("Вводить только ЦИФРЫ.")
print("Нажмите чтобы продолжить...   ")