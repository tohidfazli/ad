from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView




class AdListApiView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
    
class AdDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer



class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdByCategoryApiView(ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Ad.objects.filter(category_id=category_id)