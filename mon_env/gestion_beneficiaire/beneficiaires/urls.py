from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('gestion_bn/', views.gestion_bn, name='gestion_bn'),
    path('add_beneficiary/', views.add_beneficiary, name='add_beneficiary'),
    path('update_beneficiary/<str:cin>/', views.update_beneficiary, name='update_beneficiary'),
    path('delete_beneficiary/<str:cin>/', views.delete_beneficiary, name='delete_beneficiary'),
    path('detail_beneficiary/<str:cin>/', views.detail_beneficiary, name='detail_beneficiary'),
    path('search/',views.search_beneficiaires,name='search'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_user, name='logout'),
]
