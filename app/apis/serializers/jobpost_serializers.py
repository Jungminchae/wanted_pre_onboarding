from django.db.models import Q
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
            "position",
            "skill",
            "user",
            "company",
        )


class JobPostUpdateSerializer(JobPostSerializer):
    def validate(self, attrs):
        if "company" in attrs:
            if attrs["company"] != self.instance.company:
                raise serializers.ValidationError("채용공고의 회사 ID를 변경할 수 없음")
        return super().validate(attrs)


class JobPostReadSerializer(JobPostSerializer):
    class Meta:
        model = JobPost
        fields = (
            "id",
            "company",
            "title",
            "compensation",
            "position",
            "skill",
        )

    def to_representation(self, instance):
        representation = super(JobPostReadSerializer, self).to_representation(instance)
        representation["company"] = instance.company.name
        representation["country"] = instance.company.country
        representation["region"] = instance.company.region
        return representation


class JobPostRetrieveSerializer(JobPostReadSerializer):
    class Meta(JobPostReadSerializer.Meta):
        fields = JobPostReadSerializer.Meta.fields + ("content",)

    def to_representation(self, instance):
        other_posts = JobPost.objects.values("id").filter(
            Q(company=instance.company) & ~Q(id=instance.id)
        )
        representation = super(JobPostRetrieveSerializer, self).to_representation(
            instance
        )
        representation["other_posts"] = [i["id"] for i in other_posts]
        return representation
