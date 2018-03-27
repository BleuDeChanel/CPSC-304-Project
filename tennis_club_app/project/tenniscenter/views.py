from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Customers, Instructors, MembershipPlans
from .forms import SelectionForm

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_customers=Customers.objects.all().count()
    num_instructors=Instructors.objects.all().count()
    
    num_membership_plans=MembershipPlans.objects.count()  # The 'all()' is implied by default.
    selectionForm = SelectionForm();
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_customers':num_customers,'num_instructors':num_instructors,'num_membership_plans':num_membership_plans, 'selection_form':selectionForm},
    )


def selection(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SelectionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/tenniscenter')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SelectionForm()

    return HttpResponseRedirect('/tenniscentersss')
    # render(request, 'name.html', {'form': form})