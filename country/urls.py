from django.urls import path
from .views import CountriesListCreateAPIView,CountriesRetrieveUpdateDestroyAPIView,UniversityListCreateAPIView,UniversityRetrieveUpdateDestroyAPIView,WhyChooseListCreateAPIView,WhyChooseRetrieveUpdateDestroyAPIView,MetaTagsCountryListCreatAPIView,MetaTagsCountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('countries/',CountriesListCreateAPIView.as_view(),name="countries-list-create"),
    path('countries/<int:pk>/',CountriesRetrieveUpdateDestroyAPIView.as_view(),name="countries-retrieve-update-destroy"),
    path('university/',UniversityListCreateAPIView.as_view(),name="university-list-create"),
    path('university/<int:pk>/',UniversityRetrieveUpdateDestroyAPIView.as_view(),name="university-retrieve-update-destroy"),
    path('why-choose/',WhyChooseListCreateAPIView.as_view(),name="whychoose-list-create"),
    path('why-choose/<int:pk>/',WhyChooseRetrieveUpdateDestroyAPIView.as_view(),name="whychoose-retrieve-update-destroy"),
    path('countrymeta/',MetaTagsCountryListCreatAPIView.as_view(),name="country-list-create"),
    path('countrymeta/<int:pk>/',MetaTagsCountryRetrieveUpdateDestroyAPIView.as_view(),name="country-retrieve-update-destroy")

]