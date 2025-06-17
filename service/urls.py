from django.urls import path
from .views import ServiceBodyListCreateAPIView,ServiceBodyRetrieveUpdateDestroyAPIView,ServiceHeaderListCreateAPIView,ServiceHeaderRetrieveUpdateDestroyAPIView,MetaTagsServiceListCreateAPIView,MetaTagsServiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('service-header/',ServiceHeaderListCreateAPIView.as_view(),name="service-header-list-create"),
    path('service-header/<int:pk>/',ServiceHeaderRetrieveUpdateDestroyAPIView.as_view(),name="service-header-retrieve-update-destroy"),
    path('service-body/',ServiceBodyListCreateAPIView.as_view(),name="service-body-list-create"),
    path('service-body/<int:pk>/',ServiceBodyRetrieveUpdateDestroyAPIView.as_view(),name="service-body-retrieve-update-destroy"),
    path('servicemeta/',MetaTagsServiceListCreateAPIView.as_view(),name="servicemeta-list-create"),
    path('servicemeta/<int:pk>/',MetaTagsServiceRetrieveUpdateDestroyAPIView.as_view(),name="servicemeta-retrieve-update-destroy")
]