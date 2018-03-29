"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the tenniscenter application 
from django.urls import include

urlpatterns += [
    path('tenniscenter/', include('tenniscenter.urls')),
    path('selection/', include('tenniscenter.urls')),
    path('join/', include('tenniscenter.urls')),
    path('aggregation/', include('tenniscenter.urls')),
    path('division/', include('tenniscenter.urls')),
    path('nestedaggregation/', include('tenniscenter.urls')),
    path('deletecascade/', include('tenniscenter.urls')),
    path('deletesudentmember/', include('tenniscenter.urls')),
    
    
    
    
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/tenniscenter/')),
    path('selection/', RedirectView.as_view(url='/selection/')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
