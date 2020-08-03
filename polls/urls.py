from django.urls import path
from . import views
app_name='polls'
urlpatterns = [
    path ('',views.index,name='index'),
    
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('project/', views.project1, name='project'),
    path('work/', views.work1, name='work'),
    path('<int:id>/blog/', views.blog, name='blog'),



]