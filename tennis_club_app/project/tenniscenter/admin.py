from django.contrib import admin

# Register your models here.
from .models import ClubMemberships, CustomerRegisterPrivate, CustomerRegisterProgram, CustomerReservesCourt, Customers, Instructors, MembershipPlans, OfficeEmployees, PrivateCourseCourtReservation, PrivateTaught, ProgramCourtReservation, ProgramTaught, StudentMembers

admin.site.register(ClubMemberships)
admin.site.register(CustomerRegisterPrivate)
admin.site.register(CustomerRegisterProgram)
admin.site.register(CustomerReservesCourt)
admin.site.register(Customers)
admin.site.register(Instructors)
admin.site.register(MembershipPlans)
admin.site.register(OfficeEmployees)
admin.site.register(PrivateCourseCourtReservation)
admin.site.register(PrivateTaught)
admin.site.register(ProgramCourtReservation)
admin.site.register(ProgramTaught)
admin.site.register(StudentMembers)
