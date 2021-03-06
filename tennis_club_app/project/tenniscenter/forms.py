from django import forms

class SelectInstructors(forms.Form):
	nameChecked = forms.BooleanField(label="Name", required = False)
	phoneChecked = forms.BooleanField(label="Phone #", required = False)
	emailChecked = forms.BooleanField(label="Email", required = False)
	addressChecked = forms.BooleanField(label="Address", required = False)
	memIDChecked = forms.BooleanField(label="MemID", required = False)
	nameInput = forms.CharField(label='Name Selection', max_length=100, required = False)
	phoneInput = forms.CharField(label='Phone Selection', max_length=100, required = False)
	emailInput = forms.CharField(label='Email Selection', max_length=100, required = False)
	addressInput = forms.CharField(label='Address Selection', max_length=100, required = False)
	memIDInput = forms.CharField(label='MemID Selection', max_length=100, required = False)
	
class JoinQuery(forms.Form):
	nameInput = forms.CharField(label="Name", required = True)

class DivisionQuery(forms.Form):
	minFee = forms.CharField(label="Minimum Fee", required = True)

class AggregationQuery(forms.Form):
	aggregateChoice = forms.ChoiceField(choices=[("min","min"),("max","max"),("average","average"),("count","count")], required = True)

class NestedAggregationQuery(forms.Form):
	aggregateChoiceOne = forms.ChoiceField(choices=[("min","min"),("max","max")], required = True)
	aggregateChoiceTwo = forms.ChoiceField(choices=[("min","min"),("max","max"),("average","average"),("count","count")], required = True)

class DeleteOperationCascade(forms.Form):
	nameInput = forms.CharField(label='Name Selection', max_length=100, required = False)
	phoneInput = forms.CharField(label='Phone Selection', max_length=100, required = False)
	emailInput = forms.CharField(label='Email Selection', max_length=100, required = False)
	addressInput = forms.CharField(label='Address Selection', max_length=100, required = False)
	memIDInput = forms.CharField(label='MemID Selection', max_length=100, required = False)

class DeleteOperation(forms.Form):
	sinIDInput = forms.CharField(label='Student ID', max_length=100, required = False)

class UpdateNumberOfPeople(forms.Form):
	numOfPeople = forms.CharField(label='Number Of People', max_length=100, required = True)
	programTitle = forms.CharField(label='Program Title to update', max_length=100, required = True)


