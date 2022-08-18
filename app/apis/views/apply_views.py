from rest_framework.generics import CreateAPIView, DestroyAPIView
from apis.serializers.apply_serializers import ApplySerializer
from apis.models import Apply


class ApplyView(CreateAPIView):
    serializer_class = ApplySerializer
    queryset = Apply.objects.all()


class ApplyDeleteView(DestroyAPIView):
    queryset = Apply.objects.all()
