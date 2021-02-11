from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

app_name = 'main'

urlpatterns = [
    path('check', views.PredictView.as_view(), name='check'),
    path('tag', views.TagView.as_view(), name='tag'),
    path('train-model', views.TrainModelView.as_view(), name='train_model'),
    path('load-model', views.LoadModelView.as_view(), name='load_model'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
