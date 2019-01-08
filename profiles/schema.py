import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User


# User
class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserQuery(object):

    me = graphene.Field(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    all_users = graphene.List(UserType)

    def resolve_me(self, info, **kwargs):
        return info.context.user

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        currentUser = info.context.user
        if id != currentUser.id and not currentUser.is_staff:
            raise Exception('Authorization failed')
        if id is not None:
            return User.objects.get(pk=id)
        return None

    def resolve_all_users(self, info, **kwargs):
        currentUser = info.context.user
        if id != currentUser.id and not currentUser.is_staff:
            raise Exception('Authorization failed')
        return User.objects.all()

