from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
import logging

# Create your views here.
from .models import Customers, Instructors, MembershipPlans
from .forms import SelectInstructors, JoinQuery, AggregationQuery, DivisionQuery, NestedAggregationQuery, DeleteOperationCascade

def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_customers=Customers.objects.all().count()
	num_instructors=Instructors.objects.all().count()
	num_membership_plans=MembershipPlans.objects.count()  # The 'all()' is implied by default.

	selectInstructors = SelectInstructors();
	joinQuery = JoinQuery();
	aggregationQuery = AggregationQuery();
	divisionQuery = DivisionQuery();
	nestedAggregationQuery = NestedAggregationQuery();
	deleteOperationCascade = DeleteOperationCascade();
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'select_instructors':selectInstructors,'join_query':joinQuery,'aggregation_query':aggregationQuery,'division_query':divisionQuery,'nested_aggregation_query':nestedAggregationQuery,'delete_operation_cascade':deleteOperationCascade},
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
			
			# SQL query here
			query = "SELECT "
			if (nameChecked):
				query += "name ,"
			if (phoneChecked):
				query += "phoneNumber ,"
			if (emailChecked):
				query += "email ,"
			if (addressChecked):
				query += "address ,"
			if (memIDChecked):
				query += "membershipID ,"

			if (query[-1:] == ","):
				query = query[:-1]

			query += "FROM Customers "

			if (nameInput or phoneInput or emailInput or addressInput or memIDInput):
				query += "WHERE "
				if (nameInput):
					query += "name = '" + nameInput + "' AND "
				if (phoneInput):
					query += "name = '" + phoneInput + "' AND "
				if (emailInput):
					query += "name = '" + emailInput + "' AND "
				if (addressInput):
					query += "name = '" + addressInput + "' AND "
				if (memIDInput):
					query += "name = " + memIDInput + " AND "

			if (query[-4:] == "AND "):
				query = query[:-4]
				query += ";"

			print(query)

			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = row
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = []

			if (nameChecked):
				headers.append("Name")
			if (phoneChecked):
				headers.append("PhoneNumber")
			if (emailChecked):
				headers.append("Email")
			if (addressChecked):
				headers.append("Address")
			if (memIDChecked):
				headers.append("MembershipID")

			print(headers)

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)

	return HttpResponseRedirect('/tenniscenter/');

def join(request):
	if request.method == 'POST':
		test = JoinQuery(request.POST)
		if test.is_valid():
			# Form inputs here.
			nameInput = test['nameInput'].value()
			
			# SQL query here

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(nameInput)]
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Sample Header"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)
	return HttpResponseRedirect('/tenniscenter/');

def division(request):
	if request.method == 'POST':
		test = DivisionQuery(request.POST)
		if test.is_valid():
			# Form inputs here.
			minFee = test['minFee'].value()
			
			# SQL query here

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(minFee)]
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Sample Header"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)
	return HttpResponseRedirect('/tenniscenter/');

def aggregation(request):
	if request.method == 'POST':
		test = AggregationQuery(request.POST)
		if test.is_valid():
			# Form inputs here.
			aggregateChoice = test['aggregateChoice'].value()
			
			# SQL query here

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(aggregateChoice)]
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Sample Header"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)
	return HttpResponseRedirect('/tenniscenter/');

def nestedAggregation(request):
	if request.method == 'POST':
		test = NestedAggregationQuery(request.POST)
		if test.is_valid():
			# Form inputs here.
			aggregateChoiceOne = test['aggregateChoiceOne'].value()
			aggregateChoiceTwo = test['aggregateChoiceTwo'].value()
			
			# SQL query here

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(aggregateChoiceOne,aggregateChoiceTwo)]
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Choice1", "Choice2"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)
	return HttpResponseRedirect('/tenniscenter/');

def deleteCascade(request):
	if request.method == 'POST':
		test = DeleteOperationCascade(request.POST)
		if test.is_valid():
			# Form inputs here.
			officeSin = test['officeSin'].value()
			print(type(officeSin))
			
			query = "Delete from Office_Employees Where officesin = '" + officeSin +"'"
			# SQL query here
			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)
			# Show all the officeEmployees, showing the one deleted isn't there
			# Show program court reservation


			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = [(officeSin)]
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Choice1"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)
	return HttpResponseRedirect('/tenniscenter/');



