"""realdrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# Use include() to add paths from the patientRecord application 
# add the catalog path to the application
from django.urls import include

urlpatterns += [
    path('patientRecord/', include('patientRecord.urls')),
]

#Add URL maps to redirect the base URL to our application
#change the base url 127.0.0.1:8000 to go directly to the patientRecord app
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/patientRecord/')),
]

# Use static() to add url mapping to serve static files during development (only)
# to serve static files, like css and images during development only
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
