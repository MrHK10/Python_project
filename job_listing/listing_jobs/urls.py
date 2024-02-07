from django.contrib import admin
from django.urls import path
from listing_jobs import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='index'),
    
    
    
    
    path('login',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path("company", views.company, name='company'),
    path('dataAdd',views.dataAdd,name="dataAdd"),  #Agregar empresa a la base de datos
    path("editcompanylist",views.Editcompanylist,name="Editcompanylist"),
    path("updatecompanylist/<str:id>",views.updatecompanylist,name="updatecompanylist"),
    path('delete2/<str:id>',views.Delete2,name="delete2"),  
    
    
    
    
    path("joblisting", views.joblisting, name='joblisting'),
    path('ADD',views.ADD,name="ADD"),
    path('delete3/<str:id>',views.Delete3,name="delete3"),
    path("edit",views.Edit,name="Edit"),
    path("update/<str:id>",views.update,name="update"),
    # path("updatecompanylist/<str:id>",views.updatecompanylist,name="updatecompanylist"),
    
    
    
    
    
    path("role", views.role, name='role'),
    path("user", views.user, name='user'),
    path("source", views.source, name='source'),
    path('datasourceAdd',views.datasourceAdd,name="datasourceAdd"),
    
    path("Experience", views.Experience, name='Experience'),
    path("Employee", views.Employee, name='Employee'),
    
    
]