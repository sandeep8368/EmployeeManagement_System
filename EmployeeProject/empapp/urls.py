from empapp import views
from django.urls import path

urlpatterns = [
    path('emp/', views.display_view),
]
