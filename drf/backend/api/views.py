from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffOrReadOnly
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
# Django itself checks the user and imports it automatically. This method is good for when you have created a
# personalized user model.
from django.contrib.auth import get_user_model
from blog.models import Article


# Create your views here.

# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# better write code
# Optimizing the above codes
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # Object Filtering
    filterset_fields = ['status', 'author__username']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)
