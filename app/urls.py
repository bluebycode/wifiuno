from django.urls import path
from . import views
urlpatterns = [
    path('all',views.all,name='all'),
    path('add',views.add,name='add')
]