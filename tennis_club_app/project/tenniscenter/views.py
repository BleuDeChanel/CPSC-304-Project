from django.shortcuts import render
from django.http import HttpResponseRedirect
import logging

# Create your views here.
from .models import Customers, Instructors, MembershipPlans
from .forms import SelectInstructors

def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_customers=Customers.objects.all().count()
	num_instructors=Instructors.objects.all().count()
	num_membership_plans=MembershipPlans.objects.count()  # The 'all()' is implied by default.

	selectInstructors = SelectInstructors();
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'select_instructors':selectInstructors},
	)


def selection(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		test = SelectInstructors(request.POST)
		if test.is_valid():
			nameChecked = test['nameChecked'].value()
			phoneChecked = test['phoneChecked'].value()
			emailChecked = test['emailChecked'].value()
			addressChecked = test['addressChecked'].value()
			memIDChecked = test['memIDChecked'].value()
			nameInput = test['nameInput'].value()
			phoneInput = test['phoneInput'].value()
			emailInput = test['emailInput'].value()
			addressInput = test['addressInput'].value()
			memIDInput = test['memIDInput'].value()


			# Use above to decide what to project and select on instructors
			# SQL query here

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(nameChecked, nameInput)]

			# Set this to the number of tuples in each item in result. Here it is 2.
			tupleLength = 2

			return render(
			request,
			'display_results.html',
			context={'result':result, 'tuple_length':range(tupleLength)},
			)

	# if a GET (or any other method) we'll create a blank form
	# else:
		

	return HttpResponse("aaabbbb");






