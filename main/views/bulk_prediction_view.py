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
            serializer = BioPredictionSerializer(data=data)
            if serializer.is_valid():
                text = serializer.data['text']
                prediction = filter_handler.predict(text)
                data['predicted_label'] = prediction.get('predicted_label')
                data['probability'] = prediction.get('probability')
                data['status'] = 'ok'
                data['detail'] = 'text predicted successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def handle_uploaded_file(f):
    with open('main/filters/resources/bios2test.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
