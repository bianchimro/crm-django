from django.urls import path
from .views import ExampleView, AziendaList, AziendaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'aziende', AziendaViewSet)

urlpatterns = [
    path('example/', ExampleView.as_view(), name="example"),
    path('aziende_list/', AziendaList.as_view(), name="aziende_list"),
]

urlpatterns += router.urls
