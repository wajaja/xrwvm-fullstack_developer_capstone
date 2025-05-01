from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Authentication URLs
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # Car-related URLs
    path('get_cars/', views.get_cars, name='getcars'),
    # Dealer URLs
    path('dealers/', views.get_dealerships, name='get_dealers'),
    path('dealers/<str:state>/', views.get_dealerships, name='gt_d_by_sta'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_d'),
    # Review URLs
    path('reviews/dealer/<int:dealer_id>/', views.get_d_r, name='dealer_r'),
    path('add_review/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
