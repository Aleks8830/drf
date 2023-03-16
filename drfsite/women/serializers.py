from rest_framework import serializers

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_deta):
#         return Women.objects.create(**validated_deta)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_updata)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

# def encode():
#     model = WomenModel("Angelina", "content:Jolia")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
