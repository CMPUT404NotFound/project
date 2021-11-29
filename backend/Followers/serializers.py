
from rest_framework import serializers
from author.models import *
from backend.settings import SITE_ADDRESS


class FollowerSerializer(serializers.ModelSerializer):

    type = serializers.SerializerMethodField()

    host = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ("type", "id", "displayName", "host",
                  "url", "github", "profileImage")

    def get_type(self, obj):
        return "Follower"

    def get_host(self, obj):
        # return "temp place holder host name"
        return SITE_ADDRESS

    def get_url(self, obj: Author):
        return "placeholderserice/author/" + str(obj.id)