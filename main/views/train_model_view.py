from .utils import *


class TrainModelView(APIView):

    def get(self, request, format=None):
        filter_handler.train_fasttext_model()
        return Response(data={
            'status': 'ok',
            'detail': 'model trained successfully'
        })
