from rest_framework import generics, viewsets

from . models import blog
from . serializer import blogSerializer

# class BlogList(generics.ListAPIView):
#     queryset = blog.objects.all()
#     serializer_class = blogSerializer

# class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = blog.objects.all()
#     serializer_class = blogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=blogSerializer