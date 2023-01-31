
from django.urls import path

from todoapp import views

urlpatterns = [
    path('api',views.todo_list,name='api'),
    path('api1/<int:id>/',views.event_details,name='api'),
]
