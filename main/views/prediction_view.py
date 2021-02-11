from .utils import *

filter_handler = FilterHandler()


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
        if format == 'html':
            data = request.data
            bio_prediction_form = BioPredictionForm(data=data)
            is_valid = bio_prediction_form.is_valid()
            if is_valid:
                text = bio_prediction_form.cleaned_data.get('text')
                prediction = bio_model.my_predict(text)
                bio_prediction_form.init_predicted_label(prediction.get('predicted_label'))
                bio_prediction_form.init_probability_label(prediction.get('probability'))

            context = {
                'bio_prediction_form': bio_prediction_form,
            }
            return render(request, 'main/bio_prediction.html', context)

        else:
            pass


class TrainModelView(APIView):

    def get(self, request, format=None):
        filter_handler.train_fasttext_model()
        return Response(data={
            'status': 'ok',
            'detail': 'model trained successfully'
        })

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            data = request.data
            check_bio_form = BioPredictionForm(data=data)
            is_valid = check_bio_form.is_valid()
            if is_valid:
                text = check_bio_form.cleaned_data.get('text')
                prediction = predict(text)
                check_bio_form.init_predicted_label(prediction.get('predicted_label'))
                check_bio_form.init_probability_label(prediction.get('probability'))

            context = {
                'check_bio_form': check_bio_form,
            }
            return render(request, 'main/bio_prediction.html', context)

        else:
            pass


class LoadModelView(APIView):

    def get(self, request, format=None):
        filter_handler.load_fasttext_model()
        return Response(data={
            'status': 'ok',
            'detail': 'model loaded successfully'
        })
