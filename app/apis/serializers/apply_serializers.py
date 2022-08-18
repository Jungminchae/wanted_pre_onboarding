from rest_framework import serializers
from apis.models import Apply


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ("id", "user", "job_post")

    def validate(self, attrs):
        user = attrs.get("user")
        job_post = attrs.get("job_post")
        queryset = Apply.objects.filter(user=user, job_post=job_post)
        if queryset.exists():
            raise serializers.ValidationError("동일한 회사에는 한 번만 지원할 수 있음")
        return super().validate(attrs)
