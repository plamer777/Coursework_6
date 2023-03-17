"""This unit contains factories providing fake entities for testing purposes"""
from datetime import datetime
from faker import Faker
import factory
from ads.models import Ad, Comment
from users.models import User
# -------------------------------------------------------------------------

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """The UserFactory class creates a User models"""
    email = factory.Faker('safe_email')
    password = 'qwerty12345'
    first_name = 'John'
    last_name = 'Doe'
    is_active = True
    phone = '+79052039898'

    class Meta:
        model = User


class AdFactory(factory.django.DjangoModelFactory):
    """This factory serves to create Ad models"""
    author = factory.SubFactory(UserFactory)
    title = 'Best goods'
    description = 'You have to buy it'
    price = 1000

    class Meta:
        model = Ad


class CommentFactory(factory.django.DjangoModelFactory):
    """This factory serves to create Comment models"""
    text = 'Товар просто пушка!'
    author = factory.SubFactory(UserFactory)
    ad = factory.SubFactory(AdFactory)
    created_at = datetime.now().date()

    class Meta:
        model = Comment
