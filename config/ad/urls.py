from django.urls import path
from .views import *

app_name = 'ad'

urlpatterns = [
    path('ads/', AdListApiView.as_view()),
    path('ad/<pk>', AdDetailApiView.as_view()),
    
    
    path('category/', CategoryListApiView.as_view()),
    path('category/<int:category_id>/', AdByCategoryApiView.as_view(), name='ads-by-category'),
    # path('ad/<pk>', AdDetailApiView.as_view()),
    
    
    
]