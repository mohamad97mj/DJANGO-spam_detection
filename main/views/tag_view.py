from .utils import *


class TagView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            tag_bio_form = forms.BioTagForm()
            context = {
                'tag_bio_form': tag_bio_form
            }
            return render(request, 'main/bio_tag.html', context)
