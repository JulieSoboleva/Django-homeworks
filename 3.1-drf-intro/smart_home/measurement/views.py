from rest_framework.generics import (
    CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404
)
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import (
    SensorSerializer, MeasurementSerializer, SensorDetailSerializer
)


class SensorList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            Sensor(name=request.data['name'],
                   description=request.data['description']).save()
            return Response({'status': 'OK'})
        except:
            return Response({'status': 'Sensor not saved'})


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        try:
            sensor = get_object_or_404(Sensor, id=request.data['sensor'])
            Measurement(sensor=sensor,
                        temperature=request.data['temperature'],
                        photo=request.data.get('photo')).save()
            return Response({'status': 'OK'})
        except:
            return Response({'status': 'Measurement not saved'})
