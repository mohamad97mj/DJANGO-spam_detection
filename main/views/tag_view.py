from .utils import *


class TagView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_tag_form = forms.BioTagForm()
            context = {
                'bio_tag_form': bio_tag_form
            }
            return render(request, 'main/bio_tag.html', context)

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        data = request.data
        if format == 'html':
            bio_tag_form = BioTagForm(data=data)
            is_valid = bio_tag_form.is_valid()
            context = {
                'bio_tag_form': bio_tag_form,
            }
            if is_valid:
                instance = bio_tag_form.save(commit=False)
                instance.save()
                context.update({
                    'submitted': True,
                })

            else:
                context.update(({
                    'submitted': False,
                }))
            return render(request, 'main/bio_tag.html', context)

        elif format == 'json':
            serializer = BioTagSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                data['status'] = 'ok'
                data['detail'] = 'tag saved successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
