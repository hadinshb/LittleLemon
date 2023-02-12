from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemsView.as_view(),name='menuitems'),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
]
