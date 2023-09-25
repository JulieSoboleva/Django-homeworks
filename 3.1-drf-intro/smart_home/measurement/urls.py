from django.urls import path

from measurement.views import SensorList, SingleSensorView, MeasurementsView


urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
