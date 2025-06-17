from django.urls import path
from .views import ContactListCreateAPIView,ContactRetrieveUpdateDestroyAPIView,MetaTagsContactlistCreateAPIView,MetaTagsContactRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('contact/',ContactListCreateAPIView.as_view(),name="contact-list-create"),
    path('contact/<int:pk>/',ContactRetrieveUpdateDestroyAPIView.as_view(),name="contact-retrieve-update-destroy"),
    path('contactmeta/',MetaTagsContactlistCreateAPIView.as_view(),name="Metacontact-list-create"),
    path('contactmeta/<int:pk>/',MetaTagsContactRetrieveUpdateDestroyAPIView.as_view(),name="Metacontact-retrieve-update-destroy")
]