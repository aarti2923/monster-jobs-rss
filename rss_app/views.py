from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import json
from first.utils.postgres_connection import Postgresql
from .models import RssCategory,RssData

@api_view(['GET'])
def RssFeedCat(request):
	response = RssCategory().rss_cat_data()
	return HttpResponse(json.dumps({"status":"SUCCESS", "categories":response}), content_type="application/json")



@api_view(['GET'])
def RssFeedData(request):
	cat_id = request.query_params.get('cat_id',None)
	if cat_id == None:
		return HttpResponse(json.dumps({"status":"FAILURE", "response":'Please Provide category id!'}), content_type="application/json")

	response = RssData().rss_feed_data(cat_id)

	return HttpResponse(json.dumps({"status":"SUCCESS", "response":response}), content_type="application/json")


