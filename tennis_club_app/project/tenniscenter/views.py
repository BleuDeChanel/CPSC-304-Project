from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
import logging

# Create your views here.
from .models import Customers, Instructors, MembershipPlans
from .forms import SelectInstructors, JoinQuery, AggregationQuery, DivisionQuery, NestedAggregationQuery

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
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'select_instructors':selectInstructors,'join_query':joinQuery,'aggregation_query':aggregationQuery,'division_query':divisionQuery,'nested_aggregation_query':nestedAggregationQuery},
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
			query = "select tier from club_memberships INNER JOIN customers On club_memberships.membershipid = customers.membershipid where customers.name = '"
			query += nameInput + "';"

			print(query)
			# Pass array of results in context.
			# each tuple in the array is a result from the query
			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)

			result = row
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Tier"]

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
			query = "SELECT name FROM Instructors I WHERE NOT EXISTS ((SELECT PT.privateTitle FROM Private_taught PT WHERE PT.private_fee > "
			query += minFee + ") "
			query += "EXCEPT (SELECT PeT.privateTitle FROM Private_taught PeT WHERE PeT.insSIN=I.insSIN))"

			print(query)
			# Pass array of results in context.
			# each tuple in the array is a result from the query
			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)

			result = row
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Instructor Name"]

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
			if aggregateChoice == "average":
				query = "SELECT " + "avg" + "(fee) FROM membership_plans"
			else:
				query = "SELECT " + aggregateChoice + "(fee) FROM membership_plans"

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)

			result = row
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = []
			if aggregateChoice == "min":
				headers.append("Min")
			if aggregateChoice == "max":
				headers.append("Max")
			if aggregateChoice == "avgerage":
				headers.append("Avg")
			if aggregateChoice == "count":
				headers.append("Count")	

			print(headers)

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
			view_query = "Create View Temp(insSIN,aggfee) as SELECT PT.insSIN, "
			if aggregateChoiceTwo == "average":
				view_query += "AVG(PT.private_fee) AS aggfee FROM Private_taught PT GROUP BY PT.insSIN"
			else:
				view_query += aggregateChoiceTwo + "(PT.private_fee) AS aggfee FROM Private_taught PT GROUP BY PT.insSIN"

			query = "Select insSIN,aggfee FROM Temp WHERE aggfee =  (SELECT " + aggregateChoiceOne + "(aggfee) FROM Temp)"

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			with connection.cursor() as cursor:
				cursor.execute(view_query)
				cursor.execute(query)
				row = cursor.fetchall()
			print(row)

			result = row
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Instructor SIN", aggregateChoiceOne]
	
			with connection.cursor() as cursor:
				cursor.execute("DROP VIEW Temp")

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers},
			)

	return HttpResponseRedirect('/tenniscenter/');



