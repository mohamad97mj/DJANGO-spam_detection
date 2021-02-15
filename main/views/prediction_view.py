from .utils import *


class PredictView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_prediction_form = forms.BioPredictionForm()
            context = {
                'bio_prediction_form': bio_prediction_form
            }
            return render(request, 'main/bio_prediction.html', context)

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        data = request.data
        if format == 'html':
            bio_prediction_form = BioPredictionForm(data=data)
            is_valid = bio_prediction_form.is_valid()
            if is_valid:
                text = bio_prediction_form.cleaned_data.get('text')
                prediction = filter_handler.predict(text)
                bio_prediction_form.init_predicted_label(prediction.get('predicted_label'))
                bio_prediction_form.init_probability_label(prediction.get('probability'))

            context = {
                'bio_prediction_form': bio_prediction_form,
            }
            return render(request, 'main/bio_prediction.html', context)

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

