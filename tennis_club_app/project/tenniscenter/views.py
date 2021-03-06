from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from django.db.utils import *
import logging

# Create your views here.
from .models import Customers, Instructors, MembershipPlans
from .forms import SelectInstructors, JoinQuery, AggregationQuery, DivisionQuery, NestedAggregationQuery, DeleteOperationCascade, DeleteOperation, UpdateNumberOfPeople

def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_customers = Customers.objects.all().count()
	num_instructors = Instructors.objects.all().count()
	num_membership_plans = MembershipPlans.objects.count()  # The 'all()' is implied by default.

	selectInstructors = SelectInstructors();
	joinQuery = JoinQuery();
	aggregationQuery = AggregationQuery();
	divisionQuery = DivisionQuery();
	nestedAggregationQuery = NestedAggregationQuery();
	deleteOperationCascade = DeleteOperationCascade();
	deleteOperation = DeleteOperation();
	updateNumberOfPeople = UpdateNumberOfPeople();
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_membership_plans':num_membership_plans,'num_instructors':num_instructors,'num_customers':num_customers,'select_instructors':selectInstructors,'join_query':joinQuery,'aggregation_query':aggregationQuery,'division_query':divisionQuery,'nested_aggregation_query':nestedAggregationQuery,'delete_operation_cascade':deleteOperationCascade, 'delete_operation': deleteOperation, 'update_number_of_people': updateNumberOfPeople},
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
			
			if (nameChecked == False) and (phoneChecked == False) and (emailChecked == False) and (addressChecked == False) and (memIDChecked == False):
				return render(
						request,
						'display_results.html',
						context={'error':"Please select at least one option."},
						)

			if memIDInput != "":
				try:
					mid = int(memIDInput)
				except Exception:
					ErrorMessage = "MembershipID should be an Integer!"
					return render(
							request,
							'display_results.html',
							context={'error':ErrorMessage},
							)
			
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
					query += "phoneNumber = '" + phoneInput + "' AND "
				if (emailInput):
					query += "email = '" + emailInput + "' AND "
				if (addressInput):
					query += "address = '" + addressInput + "' AND "
				if (memIDInput):
					query += "membershipID = " + memIDInput + " AND "

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
			
			try:
				MF = int(minFee)
			except Exception:
				ErrorMessage = "minFee should be an Integer!"
				return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						)

			if int(minFee) < 0:
				ErrorMessage = "minFee should be non neggative Integer!"
				return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						)

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

def deleteCascade(request):
	if request.method == 'POST':
		test = DeleteOperationCascade(request.POST)
		if test.is_valid():
			# Form inputs here.
			nameInput = test['nameInput'].value()
			phoneInput = test['phoneInput'].value()
			emailInput = test['emailInput'].value()
			addressInput = test['addressInput'].value()
			memIDInput = test['memIDInput'].value()

			if (nameInput == "") and (phoneInput == "") and (emailInput == "") and (addressInput == "") and (memIDInput == ""):
				return render(
						request,
						'display_results.html',
						context={'error':"Nothing was deleted since no inputs were given."},
						)

			# SQL query here

			delete_query = "DELETE FROM Customers WHERE "
			
			if nameInput != "":
				delete_query += "name = '" + nameInput + "' AND "
			if phoneInput != "":
				delete_query += "phoneNumber = '" + phoneInput + "' AND "
			if emailInput != "":
				delete_query += "email = '" + emailInput + "' AND "
			if addressInput != "":
				delete_query += "address = '" + addressInput + "' AND "
			if memIDInput != "":
				try:
					memID = int(memIDInput)	
				except Exception:
					ErrorMessage = "MembershipID should be an Integer!"
					print(ErrorMessage) # maybe send the error message to the front end
					return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						) 
					delete_query += "membershipID = " + memIDInput + " AND "

			if (delete_query[-4:] == "AND "):
				delete_query = delete_query[:-4]

			print("delete_query is" + delete_query)

			# technically we should make sure both name&PN are matching as the PK is a set.
			cascade_customers = "SELECT * "
			cascade_customers += "FROM Customers WHERE "
			if nameInput != "":
				cascade_customers += "name = '" + nameInput + "' AND "
			if phoneInput != "":
				cascade_customers += "phoneNumber = '" + phoneInput + "' AND "
			if emailInput != "":
				cascade_customers += "email = '" + emailInput + "' AND "
			if addressInput != "":
				cascade_customers += "address = '" + addressInput + "' AND "
			if memIDInput != "":
				try:
					memID = int(memIDInput)	
				except Exception:
					ErrorMessage = "MembershipID should be an Integer!"
					print(ErrorMessage) # maybe send the error message to the front end
					return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						) 
				cascade_customer_reserves_court += "membershipID = " + memIDInput + " AND "

			if (cascade_customers[-4:] == "AND "):
				cascade_customers = cascade_customers[:-4]

			print(cascade_customers)
				
			# this might change later to find the matching on depending on the user's input on non primary keys
			cascade_customer_reserves_court = "SELECT * "

			matchingName = nameInput
			matchingPhoneNumber = phoneInput

			cascade_customer_reserves_court += "FROM Customer_reserves_court CRC WHERE (CRC.name, CRC.phoneNumber) = ANY (Select name, phoneNumber from Customers WHERE "

			if nameInput != "":
				cascade_customer_reserves_court += "name = '" + nameInput + "' AND "
			if phoneInput != "":
				cascade_customer_reserves_court += "phoneNumber = '" + phoneInput + "' AND "
			if emailInput != "":
				cascade_customer_reserves_court += "email = '" + emailInput + "' AND "
			if addressInput != "":
				cascade_customer_reserves_court += "address = '" + addressInput + "' AND "
			if memIDInput != "":
				try:
					memID = int(memIDInput)	
				except Exception:
					ErrorMessage = "MembershipID should be an Integer!"
					print(ErrorMessage) # maybe send the error message to the front end
					return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						) 
				cascade_customer_reserves_court += "membershipID = " + memIDInput + " AND "

			if (cascade_customer_reserves_court[-4:] == "AND "):
				cascade_customer_reserves_court = cascade_customer_reserves_court[:-4]

			cascade_customer_reserves_court += ")"
			print(cascade_customer_reserves_court)

			with connection.cursor() as cursor:
				try:
					cursor.execute(cascade_customers)
					deleted_customers = cursor.fetchall()
					print(deleted_customers)
				except Exception as err:
					print("cascade customers")
					print(err)
					return render(
						request,
						'display_results.html',
						context={'error':err},
						)

			with connection.cursor() as cursor:
				try:
					cursor.execute(cascade_customer_reserves_court)
					deleted_crc = cursor.fetchall()
					print(deleted_crc)
				except Exception as err:
					print("cascade crc")
					print(err)
					return render(
						request,
						'display_results.html',
						context={'error':err},
						)

			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = deleted_customers
			result2 = deleted_crc

			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			
			headers = ["Phone Number", "Name", "Email", "Address", "MembershipID"]
			headers2 = ["Phone Number", "Name", "Court Number", "Date", "Start Time", "End Time", "Office SIN"]

			# select and send it to the front end Then delete
			with connection.cursor() as cursor:
				try:
					cursor.execute(delete_query)
				except Exception as err:
					print(err)
					return render(
						request,
						'display_results.html',
						context={'error':err},
						)

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers, 'result2':result2, 'headers2':headers2, 'isDelete':True},
			)

	return HttpResponseRedirect('/tenniscenter/');

def deleteNoCascade(request):
	if request.method == 'POST':
		test = DeleteOperation(request.POST)
		if test.is_valid():
			# Form inputs here.
			SID = test['sinIDInput'].value()

			query = "SELECT * FROM Student_Members WHERE SID = " + SID

			if (SID == ""):
				return render(
						request,
						'display_results.html',
						context={'error':"Nothing was deleted since no inputs were given."},
						)

			try:
				sid = int(SID)	
			except Exception:
				ErrorMessage = "SID should be an Integer!"
				print(ErrorMessage) # maybe send the error message to the front end
				return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						)

			# run query first to grab the tuple
			print(query)
			with connection.cursor() as cursor:
				cursor.execute(query)
				row = cursor.fetchall()
			
			# pass the topple as result to context
			result = row
			
			query = "Delete from Student_Members Where SID = " + SID 
			# SQL query here
			with connection.cursor() as cursor:
				cursor.execute(query)
			print(query)
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["MembershipID", "SID"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers,'isDelete':True},
			)
	return HttpResponseRedirect('/tenniscenter/');

def updateNumberOfPeople(request):
	if request.method == 'POST':
		test = UpdateNumberOfPeople(request.POST)
		if test.is_valid():
			# Form inputs here.
			numOfPeople = test['numOfPeople'].value()
			try:
				numofp = int(numOfPeople)
			except Exception:
				ErrorMessage = "number of people should be an Integer!"
				print(ErrorMessage)
				return render(
						request,
						'display_results.html',
						context={'error':ErrorMessage},
						)
				
			programTitle = test['programTitle'].value()
			
			if numOfPeople != "":
				query1 = "UPDATE Program_taught SET numberOfPeople = " + numOfPeople + " WHERE programTitle = '" + programTitle + "'"
			# SQL query here
			print(query1)
			with connection.cursor() as cursor:
				try:
					cursor.execute(query1)
				except Exception as err:
					print("Make sure the number of people is greater than or equal to 2")
					print(err)
					return render(
						request,
						'display_results.html',
						context={'error':err},
						)

			# Show all the officeEmployees, showing the one deleted isn't there
			# Show program court reservation
			query = "SELECT * from Program_taught"
			print(query)
			with connection.cursor() as cursor:
				try:
					cursor.execute(query)
					updated_program_taught = cursor.fetchall() # not certain if this is where it belongs but think it is
				except Exception as err: # the error should be smt from sql
					print(err)
					return render(
						request,
						'display_results.html',
						context={'error':err},
						)

			
			# Pass array of results in context.
			# each tuple in the array is a result from the query
			result = updated_program_taught
			# The headers for the columns (Ensure length of headers is same for the # of items in each tuple of result)
			headers = ["Program Title", "Number Of People" , "Fee", "Start Date", "End Date", "Instructor SIN"]

			return render(
			request,
			'display_results.html',
			context={'result':result,'headers':headers,'isUpdate':True},
			)
	return HttpResponseRedirect('/tenniscenter/');