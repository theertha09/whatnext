from django.urls import path
from .views import VoiceOfSuccessListCreateAPIView,VoiceOfSuccessListView,VoiceOfSuccessRetrieveUpdateDestroyAPIView,StudentReviewListCreateAPIView,StudentReviewRetrieveUpdateDestroyAPIView,MetaTagsHomeListCreateAPIView,MetaTagsHomeRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('video/',VoiceOfSuccessListCreateAPIView.as_view(),name= 'voiceofsuccess-list-create'),
    path('videos/get/',VoiceOfSuccessListView.as_view(),name="voiceofsuccess-list-get"),
    path('video/<int:pk>/',VoiceOfSuccessRetrieveUpdateDestroyAPIView.as_view(),name="voiceofsuccess-retrieve-update-destroy"),
    path('student-review/',StudentReviewListCreateAPIView.as_view(),name="student-review-list-create"),
    path('student-review/<int:pk>/',StudentReviewRetrieveUpdateDestroyAPIView.as_view(),name="student-review-retrieve-update-destroy"),
    path('MetaTagsHome/',MetaTagsHomeListCreateAPIView.as_view(),name="metatagshome-list-create"),
    path('MetaTagsHome/<int:pk>/',MetaTagsHomeRetrieveUpdateDestroyAPIView.as_view(),name="metatagshome-retrieve-update-destroy")
]