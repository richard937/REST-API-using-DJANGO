from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

class StockList(APIView): # in bracket we write from where we are going to inherit
	
	def get(self,request):  
		stocks = Stock.objects.all()
		serializer =  StockSerializer(stocks,many = True)
		return Response(serializer.data)
	def post(self):
		pass 


# THE MAIN ADVANTAGE OF DJANGO THAT WE CAN ACCESS OUR DATA OF DATABASE IN JSON FORMAT FROM ANY PLATFORM
# AS WINDOWS , ANDROID , IOS OR OTHER WITH THE SAME URL

