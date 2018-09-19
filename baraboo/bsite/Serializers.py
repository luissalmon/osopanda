from bsite.PresentationProject import PresentationProject
from rest_framework import serializers


class PresentationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PresentationProject
        fields = ('idProject',
        'title',
        'description',
        'returnOfInversion',
        'expirationDate',
        'initialInvestmentRound',
        'taretCapital',
        'video',
        'presentation',
        'images',
        )
