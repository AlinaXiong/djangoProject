from django.urls import path

from .views import MatrixTransposeAPIView

urlpatterns = [
    path('reachability/warshall-calculate', MatrixTransposeAPIView.as_view(),
         name='use warshall_algorithm to calculate reachability matrix'),
]
