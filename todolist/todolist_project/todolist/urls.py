from django.urls import path,include
from . import views

app_name ='todolist'

urlpatterns = [
    path("",views.home,name='home'),
    path("create/",views.create_todo,name='create-todo'),
    path("delete/<int:id>",views.delete_todo,name='delete-todo'),
    path("update/<int:id>",views.update_todo,name='update-todo'),
    path("finished/<int:id>",views.finished_task,name='finished-todo'),
    path('unfinished/<int:id>',views.unfinished_task,name='unfinished-todo'),
]
