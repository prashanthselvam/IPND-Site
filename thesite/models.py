from django.db import models
from django.utils import timezone
import calendar
import datetime
from datetime import date
from datetime import time

class GuestBookPost(models.Model):
	author = models.CharField(max_length = 40)
	text = models.TextField()
	date = models.DateTimeField(
		default = timezone.now)

	def post(self):
		self.save()

	def __str__(self):
		return self.author



class SumOfDays(models.Model):

	def is_leap(self,year):
		days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
		if calendar.isleap(year):
			days_of_months[1] = 29
		else:
			days_of_months[1] = 28

	def valid_year(self,year):
		if year and year.isdigit() and int(year) in range(1900, date.today().year + 1):
			return int(year)

	def valid_month(self,month):
		if month and month.isdigit() and int(month) in range(1,13):
			return int(month)

	def valid_day(self,day,month,year):
		days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]
		SumOfDays().is_leap(int(year))
		n = int(month)-1
		if day and day.isdigit() and int(day) <= days_of_months[n]:
			return int(day)

	def days(self,year,month,day):
		d1 = datetime.date(year,month,day)
		d2 = datetime.date.today()
		days = d2 - d1
		days = str(days)[0:str(days).find(' ')]
		return days