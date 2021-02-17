from .utils import *


class PredictionView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_prediction_form = BioPredictionForm()
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
            context = {
                'bio_prediction_form': bio_prediction_form,
            }
            if is_valid:
                bio = bio_prediction_form.cleaned_data.get('bio')
                prediction = filter_handler.predict(bio)
                bio_prediction_form.init_predicted_label(prediction.get('predicted_label'))
                bio_prediction_form.init_probability(prediction.get('probability'))
                bio_prediction_form.init_predicted_by(prediction.get('predicted_by'))

            return render(request, 'main/bio_prediction.html', context)

        elif format == 'json':
            serializer = BioPredictionSerializer(data=data)
            if serializer.is_valid():
                bio = serializer.data['bio']
                prediction = filter_handler.predict(bio)
                data['predicted_label'] = prediction.get('predicted_label')
                data['probability'] = prediction.get('probability')
                data['predicted_by'] = prediction.get('predicted_by')
                data['status'] = 'ok'
                data['detail'] = 'bio predicted successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
