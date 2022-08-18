from rest_framework.generics import CreateAPIView
from apis.serializers.apply_serializers import ApplySerializer
from apis.models import ApplyList


class ApplyView(CreateAPIView):
    serializer_class = ApplySerializer
    queryset = ApplyList.objects.all()
