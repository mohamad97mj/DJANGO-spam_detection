from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

app_name = 'main'

urlpatterns = [
    path('predict', views.PredictionView.as_view(), name='predict'),
    path('bulk-predict', views.BulkPredictionView.as_view(), name='bulk_predict'),
    path('tag', views.TagView.as_view(), name='tag'),
    path('test', views.TestView.as_view(), name='test'),
    path('train-model', views.TrainModelView.as_view(), name='train_model'),
    path('load-model', views.LoadModelView.as_view(), name='load_model'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
