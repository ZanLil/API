from django.urls import path
from . import views

urlpatterns = [
    path('v1/submit-data/', views.SubmitDataView.as_view())
]
