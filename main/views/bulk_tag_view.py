from .utils import *


class BulkTagView(APIView):
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def get(self, request, format=None):
        format = request.accepted_renderer.format
        if format == 'html':
            bio_bulk_tag_form = BioBulkTagForm
            context = {
                'bio_bulk_tag_form': bio_bulk_tag_form
            }
            return render(request, 'main/bio_bulk_tag.html', context)

    def post(self, request, format=None):
        format = request.accepted_renderer.format
        data = request.data
        if format == 'html':
            bio_bulk_tag_form = BioBulkTagForm(request.POST, request.FILES)
            is_valid = bio_bulk_tag_form.is_valid()
            context = {
                'bio_bulk_tag_form': bio_bulk_tag_form,
            }
            if is_valid:
                file = request.FILES['file']
                tags_df = FileUtils.read_excel_file(file)
                tag_bios(tags_df)
                context.update({
                    'status': 'ok',
                })

            else:
                context.update(({
                    'status': 'nok',
                }))
            return render(request, 'main/bio_bulk_tag.html', context)

        elif format == 'json':
            serializer = SingleFileSerializer(request.POST, request.FILES)
            if serializer.is_valid():
                file = request.FILES['file']
                tags_df = FileUtils.read_excel_file(file)
                tag_bios(tags_df)
                data['status'] = 'ok'
                data['detail'] = 'bios tagged successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def tag_bios(tags):
    for index, row in tags.iterrows():
        bio = row['bio']
        label = row['label']
        Tag.objects.create(bio=bio, label=label)
