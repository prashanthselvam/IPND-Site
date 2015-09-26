from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import GuestBookPost
from .models import SumOfDays
from .forms import GuestBookForm

# Create your views here.
def home(request):
	return render(request, 'thesite/home.html', {})

def notes(request):
	return render(request, 'thesite/notes.html', {})

def age_in_days(request):
	if request.method == "POST":
		instance = SumOfDays()
		day = request.POST.get('day')
		month = request.POST.get('month')
		year = request.POST.get('year')
		
		year = instance.valid_year(year)
		month = instance.valid_month(month)
		if year and month:
			day = instance.valid_day(day,month,year)
			if not day:
				return render(request, 'thesite/age_in_days.html', {'error':'Invalid Date! Please try again.'})
			else:
				age = str(instance.days(year,month,day))
				return render(request, 'thesite/age_in_days.html', {'r':age})
		else:
			return render(request, 'thesite/age_in_days.html', {'error':'Please enter a valid date!'})
	else:
		return render(request, 'thesite/age_in_days.html', {'msg':'Give it a shot!'})

def guestbook(request):
	if request.method == "POST":
		form = GuestBookForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.date = timezone.now()
			post.save()
			return redirect('thesite.views.guestbook')
	else:
		form = GuestBookForm()
	posts = GuestBookPost.objects.filter(date__lte=timezone.now()).order_by('-date')[0:5]
	return render(request, 'thesite/guestbook.html', {'posts':posts, 'form':form})