
from django.urls import path

from .views import index_view , result_view

app_name = 'core'

urlpatterns = [
    
    # url for upload image
    path('' , index_view , name = 'index'),

    # url for see result of proccess on image
    path('result/' , result_view , name = 'result'),

]
