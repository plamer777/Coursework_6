"""This unit contains CBVs for advertisements and comments"""
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.utils.translation import gettext_lazy as _
from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import UpdateDeleteAdPermission, \
    UpdateDeleteCommentPermission, AdminPermission
from ads.serializers import AdSerializer, CommentSerializer, \
    AdRetrieveCreateUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
# --------------------------------------------------------------------------


class AdPagination(pagination.PageNumberPagination):
    """AdPagination class serves as a paginator"""
    page_size = 4


@extend_schema_view(
    list=extend_schema(
        description=_(
            'Returns a list of advertisements sorted by creation date'),
        summary=_('A list of advertisements')
    ),
    retrieve=extend_schema(description=_('Returns a detail advertisement'),
                           summary=_('A detail advertisement')
                           ),
    create=extend_schema(description=_(
        'Adds a new advertisement to the database'),
                           summary=_('Add advertisement')
                           ),
    update=extend_schema(description=_(
        'Updates all fields of the certain advertisement'),
                           summary=_('Update advertisement')
                           ),
    partial_update=extend_schema(description=_(
        'Updates chosen fields of the certain advertisement'),
                           summary=_('Partially update advertisement')
                           ),
    destroy=extend_schema(description=_(
        'Deletes the advertisement from the database'),
                           summary=_('Delete advertisement')
                           ),
)
class AdViewSet(viewsets.ModelViewSet):
    """AdViewSet class is a main view providing CRUD operations for
    advertisements"""
    queryset = Ad.objects.order_by('-created_at')
    default_serializer = AdRetrieveCreateUpdateSerializer
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter
    default_permissions = [AllowAny]

    serializers = {'list': AdSerializer}
    permissions = {'retrieve': [IsAuthenticated],
                   'create': [IsAuthenticated],
                   'update': [UpdateDeleteAdPermission | AdminPermission],
                   'destroy': [UpdateDeleteAdPermission | AdminPermission],
                   'partial_update': [
                       UpdateDeleteAdPermission | AdminPermission]
                   }

    def get_permissions(self):
        """This method was overdetermined to be able to work with different
        permissions"""
        return [permission() for permission in self.permissions.get(
            self.action, self.default_permissions)]

    def get_serializer_class(self):
        """This method was overdetermined to be able to work with different
        serializers"""
        return self.serializers.get(self.action, self.default_serializer)


@extend_schema(description=_('Returns a list of user\'s advertisements'),
               summary=_('A list of user\'s advertisements'))
class UserAdsView(ListAPIView):
    """This CBV was created to return a list of advertisements of current
    authenticated user"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def get_queryset(self):
        """Overdetermined method to return Ad models for current user"""
        author_id = self.request.user.pk
        return Ad.objects.filter(author_id=author_id).order_by('-created_at')


@extend_schema_view(
    list=extend_schema(
        description=_(
            'Returns a list of all comments'),
        summary=_('A list of comments')
    ),
    retrieve=extend_schema(description=_('Returns a detail comment'),
                           summary=_('A detail comment')
                           ),
    create=extend_schema(description=_(
        'Adds a new comment to the database'),
                           summary=_('Add comment')
                           ),
    update=extend_schema(description=_(
        'Updates all fields of the certain comment'),
                           summary=_('Update comment')
                           ),
    partial_update=extend_schema(description=_(
        'Updates chosen fields of the certain comment'),
                           summary=_('Partially update comment')
                           ),
    destroy=extend_schema(description=_(
        'Deletes the comment from the database'),
                           summary=_('Delete comment')
                           ),
)
class CommentViewSet(viewsets.ModelViewSet):
    """This ViewSet provides CRUD operations for Comment objects"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    default_permissions = [IsAuthenticated]
    permissions = {'list': [IsAuthenticated],
                   'create': [IsAuthenticated],
                   'update': [UpdateDeleteCommentPermission | AdminPermission],
                   'destroy': [UpdateDeleteCommentPermission | AdminPermission],
                   'partial_update': [
                       UpdateDeleteCommentPermission | AdminPermission]
                   }

    def get_queryset(self):
        """This method returns a comment's queryset for current Ad model"""
        pk = self.kwargs.get('uid')
        return Comment.objects.filter(ad_id=pk)

    def get_permissions(self):
        """This method returns a list of permissions for certain action"""
        return [permission() for permission in self.permissions.get(
            self.action, self.default_permissions)]
