from django.urls import path
from . import views


app_name='reader-urls'
urlpatterns = [
    path('login/', views.Login.as_view(), name='reader-login'),
    path('<int:pk>', views.detail_reader, name='detail-reader')
]