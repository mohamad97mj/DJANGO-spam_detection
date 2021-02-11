from utils import *


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['text', 'predicted_label', 'probability']


