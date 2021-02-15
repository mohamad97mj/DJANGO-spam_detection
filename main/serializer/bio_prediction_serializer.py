from main.serializer.utils import *


class BioPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['text', 'predicted_label', 'probability']
        extra_kwargs = {
            'predicted_label': {'required': False},
            'probability': {'required': False},
        }
