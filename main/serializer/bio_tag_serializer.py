from main.serializer.utils import *


class BioTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['bio', 'label']

