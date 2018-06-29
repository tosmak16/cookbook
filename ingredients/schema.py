import graphene
from graphene_django.types import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category


class IngredientType(DjangoObjectType):

    class Meta:
        model = Ingredient


class Query(object):
    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())

    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_category(self, info, **kwargs):

        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)
        return None

    def resolve_ingredient(self, info, **kwargs):

        id = kwargs.get('id')

        if id is None:
            return Ingredient.objects.get(pk=id)
        return None
