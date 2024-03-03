from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_list),
    path('<int:pk>', views.URL_DetailView.as_view(), name='course-detail'),
]