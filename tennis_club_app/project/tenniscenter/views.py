from django.shortcuts import render

# Create your views here.
from .models import Customers, Instructors, MembershipPlans

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_customers=Customers.objects.all().count()
    num_instructors=Instructors.objects.all().count()
    
    num_membership_plans=MembershipPlans.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_customers':num_customers,'num_instructors':num_instructors,'num_membership_plans':num_membership_plans},
    )
