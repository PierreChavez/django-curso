from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data={'data': serializer.data})
#
#     def retrieve(self, request, pk=int):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post)
#         return Response(status=status.HTTP_200_OK, data={'data': serializer.data})
#
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid data', 'errors': serializer.errors})
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data={'message': 'Post created', 'data': serializer.data})
        
# class PostApiView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data={'data': serializer.data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid data', 'errors': serializer.errors})
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data={'message': 'Post created', 'data': serializer.data})


