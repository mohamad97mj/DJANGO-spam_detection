from .utils import *


class WelcomeView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        context = {
        }
        return Response(context, template_name='main/welcome.html')



