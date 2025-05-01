from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

D_R_PATH = 'reviews/dealer/<int:dealer_id>/'
D_ID_PATH = 'dealer/<int:dealer_id>/'
D_ST_PATH = 'dealers/<str:state>/'

urlpatterns = [
    # Authentication URLs
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # Car-related URLs
    path('get_cars/', views.get_cars, name='getcars'),
    # Dealer URLs
    path('dealers/', views.get_dealerships, name='get_dealers'),
    path(D_ST_PATH, views.get_dealerships, name='get_dealers_by_state'),
    path(D_ID_PATH, views.get_dealer_details, name='dealer_details'),
    # Review URLs
    path(D_R_PATH, views.get_dealer_reviews, name='dealer_r'),
    path('add_review/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
