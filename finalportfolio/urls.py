from django.urls import path
from . import views
app_name='finalportfolio'
urlpatterns = [
    path ('',views.index,name='index'),
    path ('work/',views.work,name='work'),
      path ('projects/',views.projects,name='projects'),
]