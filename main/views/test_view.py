from .utils import *


class TestView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_test_form = BioTestForm()
            context = {
                'bio_test_form': bio_test_form
            }
            return render(request, 'main/bio_test.html', context)

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_test_form = BioTestForm(request.POST, request.FILES)
            context = {
                'bio_test_form': bio_test_form,
            }
            if bio_test_form.is_valid():
                file = request.FILES['file']
                test_results = filter_handler.test(file)
                bio_test_form.init_precision(test_results.get('precision'))
                bio_test_form.init_recall(test_results.get('recall'))
            return render(request, 'main/bio_test.html', context)

        elif format == 'json':
            serializer = BioPredictionSerializer(data=data)
            if serializer.is_valid():
                bio = serializer.data['bio']
                test_results = filter_handler.test(bio)
                data['precision'] = test_results.get('precision')
                data['recall'] = test_results.get('recall')
                data['status'] = 'ok'
                data['detail'] = 'filter tested successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


