def is_leap_(year):
	if (year % 400 == 0) or (year % 100 != 0 year % 4 == 0):
		return True
	else:
		return False
a = int(input('請輸入年:'))
print(is_leap_year(a))
