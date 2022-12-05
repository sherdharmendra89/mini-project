from django.contrib import admin
from django.urls import path
from ORS import views


urlpatterns = [
    path('', views.index),
    # path('<page>/<action>/', views.action),
    path('auth/<page>/', views.auth),
    path('<page>/', views.actionId),
    path('<page>/<operation>/<int:id>',views.actionId)
]