
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import UniqueidTable, DataTable
from .serializers import UniqueEndpointCreateSerializer, DataSerializer, ListActiveUniqueEndpointsSerializer, DetailEndpointSerializer
import logging
import datetime
import uuid


logger = logging.getLogger(__name__)


class CreateUniqueEndpoint(APIView):
    
    def get(self, request):
        from scheduler.background_tasks import cleanup
        base_table = UniqueidTable(uniqueid=str(uuid.uuid4()))
        base_table.url = request.build_absolute_uri().split("create")[0]+base_table.uniqueid
        base_table.save()
        logger.info("Unique ID generated & saved to DB {}".format(base_table.uniqueid))
        delete_time = datetime.datetime.now()+datetime.timedelta(minutes=5)
        cleanup(base_table.uniqueid, delete_time)
        logger.info("{} has been scheduled to be removed in 60 mins from now {}".format(base_table.uniqueid, delete_time))
        serialized_data = UniqueEndpointCreateSerializer(UniqueidTable.objects.get(uniqueid=base_table.uniqueid))
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class ListActiveUniqueEndpoints(APIView):

    def get(self, request):
        if not len(UniqueidTable.objects.all())>1:
            return JsonResponse({"message":"No resources have been created yet"}, status=status.HTTP_404_NOT_FOUND)
        serialized_data = ListActiveUniqueEndpointsSerializer(data=UniqueidTable.objects.all())
        if serialized_data.is_valid():
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors)


class DetailEndpoint(APIView):

    def get(self, request, uniqueid):
        if not UniqueidTable.objects.filter(uniqueid=uniqueid):
            return JsonResponse({"message":"No such resources found, check your uniqueid"}, status=status.HTTP_404_NOT_FOUND)
        bt = UniqueidTable.objects.get(uniqueid=uniqueid)
        bt.hits = bt.hits+1
        bt.save()
        data = DataTable.objects.filter(uniqueid=UniqueidTable.objects.get(uniqueid=uniqueid))
    
        if not data:
            return JsonResponse({"message":"No data has been pushed yet!"}, status=status.HTTP_204_NO_CONTENT)
        serialized_data = DetailEndpointSerializer(data=data)
        if serialized_data.is_valid():
            return JsonResponse(serialized_data.data, status=status.HTTP_200_OK, safe=False)
        return Response(serialized_data.errors)

class PostData(GenericAPIView):
    serializer_class = DataSerializer
    def post(self, request, uniqueid):
        if not UniqueidTable.objects.filter(uniqueid=uniqueid):
            return JsonResponse({"message":"No such resources found, check your uniqueid"}, status=status.HTTP_404_NOT_FOUND)
        bt = UniqueidTable.objects.get(uniqueid=uniqueid)
        bt.hits = bt.hits+1
        bt.save()
        serializer_data = DataSerializer(data=request.data)
        if serializer_data.is_valid():
            dt = DataTable(uniqueid=UniqueidTable.objects.get(uniqueid=uniqueid), data=request.data["data"])
            dt.save()
        return JsonResponse(serializer_data.data, status=status.HTTP_201_CREATED)
