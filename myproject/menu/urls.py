from django.urls import path

from .views import IndexPageView

app_name = 'menu_app'


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
