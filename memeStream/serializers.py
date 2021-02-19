from rest_framework import serializers
from memeStream.models import Meme

class MemeSerializer(serializers.ModelSerializer):

    # overriding the model fields with new having some styling parameters like placeholder
    url = serializers.URLField(style={
        "placeholder": "Meme Url"
    })
    name = serializers.CharField(style={
        "placeholder": "Owner name"
    })
    caption = serializers.CharField(style={
        "placeholder": "Caption"
    })

    # defining the meta class for setting the model and fields for the serialiser
    class Meta:
        model = Meme
        fields = ["id", "name", "url", "caption"]