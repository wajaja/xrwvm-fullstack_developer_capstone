"""
djangoproj URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Django app API endpoints
    path('api/', include('djangoapp.urls')),

    # Static pages
    path('',
    TemplateView.as_view(template_name="Home.html"),
    name='home'),
    path('about/',
    TemplateView.as_view(template_name="About.html"),
    name='about'),
    path('contact/',
        TemplateView.as_view(template_name="Contact.html"),
        name='contact'),

    # Frontend routes (handled by React)
    path('login/',
        TemplateView.as_view(template_name="index.html"),
        name='login'),
    path('register/',
        TemplateView.as_view(template_name="index.html"),
        name='register'),
    path('dealers/',
        TemplateView.as_view(template_name="index.html"),
        name='dealers'),

    # Dynamic frontend routes
    path('dealer/<int:dealer_id>/',
        TemplateView.as_view(template_name="index.html"),
        name='dealer_detail'),
    path('postreview/<int:dealer_id>/',
        TemplateView.as_view(template_name="index.html"),
        name='post_review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
