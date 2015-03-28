from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from collection.models import Collection
from collection_user.models import SCUser
from collection_user.serializers import SCUserSerializer


class CollectionSerializer(serializers.ModelSerializer):
	author = SCUserSerializer(read_only=True, required=False)

	class Meta:
		model = Collection

		fields = ('collection_name', 'author', 'collection_description',
					'item', 'created_at', 'updated_at')

		read_only_fields = ('created_at', 'updated_at')

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(CollectionSerializer, self).get_validation_exclusions()

		return exclusions + ['author']