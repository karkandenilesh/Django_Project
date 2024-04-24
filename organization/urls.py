from django.urls import path
from . import views
from .views import FilterOrganizations

urlpatterns = [
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('query/', views.query, name='query'),
    path('user/', views.user_list, name='user_list'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('filt/', views.filter_organizations, name='filt'),
    path('add_user/', views.add_user, name='add_user'),
    path('api/filter-organizations/', FilterOrganizations.as_view(), name='filter_organizations_api'),
    path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]