"""
djangoproj URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView as T
from django.conf.urls.static import static
from django.conf import settings

REVIEW_PATH = 'postreview/<int:id>/'

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Django app API endpoints
    path('api/', include('djangoapp.urls')),

    # Static pages
    path('', T.as_view(template_name="Home.html"), name='home'),
    path('about/', T.as_view(template_name="About.html"), name='about'),
    path('contact/', T.as_view(template_name="Contact.html"), name='contact'),

    # Frontend routes (handled by React)
    path('login/', T.as_view(template_name="index.html"), name='login'),
    path('register/', T.as_view(template_name="index.html"), name='register'),
    path('dealers/', T.as_view(template_name="index.html"), name='dealers'),

    # Dynamic frontend route
    path('dealer/<int:id>/', T.as_view(template_name="index.html"), name='d'),
    path(REVIEW_PATH, T.as_view(template_name="index.html"), name='p'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
