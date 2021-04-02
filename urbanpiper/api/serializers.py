from rest_framework import serializers
from api.models import DataTable, UniqueidTable


class UniqueEndpointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueidTable
        fields = ["url", "created_at", "active_state", "hits"]


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = ["data"]


class ListActiveUniqueEndpointsSerializer(serializers.BaseSerializer):
    # active_endpoints = serializers.StringRelatedField(many=True)
    def to_representation(self, instance):
        return [{"url":x.url, "hits": x.hits, "createdAt": x.created_at} for x in instance]

    def to_internal_value(self, data):
        return data


class DetailEndpointSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return [{"data": x.data for x in instance}]

    def to_internal_value(self, data):
        return data
    