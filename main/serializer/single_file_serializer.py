from main.serializer.utils import *


class SingleFileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)
