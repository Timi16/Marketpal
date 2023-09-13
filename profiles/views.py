from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Farmer, Buyer,Product
from .serializers import FarmerSerializer, BuyerSerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated
class FarmerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        farmer = Farmer.objects.get(pk=pk)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

class BuyerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        buyer = Buyer.objects.get(pk=pk)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)

class ProductListView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
        
class FarmerProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, farmer_pk, product_pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FarmerProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyerProductSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q')  # Get the search query from the request
        if search_query:
            # Perform a case-insensitive search on the product name using icontains
            products = Product.objects.filter(name__icontains=search_query)
            if products.exists():
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)
            else:
                return Response({"message": "No products found for the query"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST)