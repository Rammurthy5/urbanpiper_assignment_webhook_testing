from django.urls import path, include
from .views import CreateUniqueEndpoint, ListActiveUniqueEndpoints, DetailEndpoint, PostData

urlpatterns = [
    path('webhook-testing/v1/endpoints/create', CreateUniqueEndpoint.as_view(), name="Create Endpoint"),
    path('webhook-testing/v1/endpoints/', ListActiveUniqueEndpoints.as_view(), name="List Active Endpoints"),
    path('webhook-testing/v1/endpoints/<str:uniqueid>', DetailEndpoint.as_view(), name="Detail a given Endpoint"),
    path('webhook-testing/v1/endpoints/<str:uniqueid>/post', PostData.as_view(), name="Post data to webhook"),
]
