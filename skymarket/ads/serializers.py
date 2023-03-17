"""This unit contains serializers to implement CRUD operations with Ad and
Comment models"""
from rest_framework import serializers
from ads.models import Comment, Ad
# --------------------------------------------------------------------------


class CommentSerializer(serializers.ModelSerializer):
    """CommentSerializer class for all operations with Comment model"""
    author_id = serializers.IntegerField(
        read_only=True, required=False)
    author_first_name = serializers.CharField(
        read_only=True, required=False)
    author_last_name = serializers.CharField(
        read_only=True, required=False)
    author_image = serializers.ImageField(
        read_only=True, required=False)

    class Meta:
        model = Comment
        fields = ('pk', 'ad_id', 'author_id',
                  'author_first_name', 'author_last_name',
                  'author_image', 'text', 'created_at')

    def create(self, validated_data):
        user = self.context.get('request').user
        ad_id = self.context.get('view').kwargs.get('uid')

        validated_data['author'] = user
        validated_data['ad_id'] = int(ad_id)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user
        validated_data['ad'] = instance.ad

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ava = instance.author.image
        data['author_first_name'] = instance.author.first_name
        data['author_last_name'] = instance.author.last_name
        data['author_image'] = ava.url if ava else None

        return data


class AdSerializer(serializers.ModelSerializer):
    """AdSerializer class is used to only for list action"""
    class Meta:
        model = Ad
        fields = ('image', 'title', 'description', 'price', 'pk')


class AdRetrieveCreateUpdateSerializer(serializers.ModelSerializer):
    """This serializer is used to implement all the operations with Ad model
    except list action"""
    author_id = serializers.PrimaryKeyRelatedField(
        read_only=True, required=False)
    author_first_name = serializers.CharField(
        read_only=True, required=False)
    author_last_name = serializers.CharField(
        read_only=True, required=False)
    phone = serializers.CharField(
        read_only=True, required=False)

    class Meta:
        model = Ad
        fields = ('pk', 'title',
                  'description', 'price', 'image',
                  'phone', 'author_id', 'author_first_name',
                  'author_last_name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_first_name'] = instance.author.first_name
        data['author_last_name'] = instance.author.last_name
        data['phone'] = str(instance.author.phone)
        return data

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user

        return super().update(instance, validated_data)
