from typing import Union
from django.shortcuts import render

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpRequest
from author.token import TokenAuth
from nodes.models import Node

from nodes.serializers import NodeSerializer
# Create your views here.



@api_view(["GET"])
@authentication_classes([TokenAuth(bypassEntirely=["GET"])])
def getNodes(request: Union[Request, HttpRequest]) -> Response:
    
    if request.method == "GET":
        return Response(NodeSerializer(Node.objects.all(), many = True).data, status=200)
    
    