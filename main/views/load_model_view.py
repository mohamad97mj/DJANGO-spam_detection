from .utils import *


class LoadModelView(APIView):

    def get(self, request, format=None):
        filter_handler.load_fasttext_model()
        return Response(data={
            'status': 'ok',
            'detail': 'model loaded successfully'
        })
