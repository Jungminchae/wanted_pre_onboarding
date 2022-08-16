from rest_framework import serializers
from apis.models import JobPost


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = (
            "id",
            "title",
            "content",
            "compensation",
            "skill",
            "user",
            "company",
        )
