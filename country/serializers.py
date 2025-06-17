from rest_framework import serializers
from .models import Countries,WhyChoose,University,MetaTagsCountry

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"

class WhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = "__all__"

class CountriesSerializer(serializers.ModelSerializer):
    universities = UniversitySerializer(many=True, read_only=True)
    why_choose_reasons = WhyChooseSerializer(many=True, read_only=True)

    class Meta:
        model = Countries
        fields = '__all__'

class MetaTagsCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsCountry
        fields = "__all__"

