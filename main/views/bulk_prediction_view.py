from .utils import *


class BulkPredictionView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_bulk_prediction_form = BioBulkPredictionForm()
            context = {
                'bio_bulk_prediction_form': bio_bulk_prediction_form
            }
            return render(request, 'main/bio_bulk_prediction.html', context)

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_bulk_prediction_form = BioBulkPredictionForm(request.POST, request.FILES)
            is_valid = bio_bulk_prediction_form.is_valid()
            context = {
                'bio_bulk_prediction_form': bio_bulk_prediction_form,
            }
            if is_valid:
                file = request.FILES['file']
                filter_handler.bulk_predict(file)
                context.update({
                    'status' : 'ok'
                })

            return render(request, 'main/bio_bulk_prediction.html', context)

        elif format == 'json':
            serializer = SingleFileSerializer(request.POST, request.FILES)
            if serializer.is_valid():
                file = request.FILES['file']
                filter_handler.bulk_predict(file)
                prediction_file = open('media/predictions.xlsx', 'rb')
                response = HttpResponse(prediction_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="%s"' % 'predictions.xlsx'
                return response
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


