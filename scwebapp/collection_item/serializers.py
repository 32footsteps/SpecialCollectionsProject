from rest_framework import serializers

from collection_user.serializers import SCUserSerializer
from collection_item.model import Item

class ItemSerializer(serializers.ModelSerializer):
	creator = SCUserSerializer(read_only=True, required=False)

	class Meta:
		model = Item

		fields = ('id', 'title', 'creator', 'subject', 'description', 
			'publisher', 'contributor', 'date', 'item_type', 'item_format',
			'identifer', 'source', 'language', 'relation', 'coverage', 'rights',
			'updated_at', 'item_image')
		read_only_fields = ('id', 'date', 'updated_at')

		def create(self, validated_data):
			return Item.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.title = validated_data.get('title', instance.title)
			instance.subject = validated_data.get('subject', instance.subject)
			instance.description = validated_data.get('description', instance.description)
			instance.publisher = validated_data.get('publisher', instance.publisher)
			instance.contributor = validated_data.get('contributor', instance.contributor)
			instance.item_type = validated_data.get('item_type', instance.item_type)
			instance.item_format = validated_data.get('item_format', instance.item_format)
			instance.identifer = validated_data.get('identifer', instance.identifer)
			instance.source = validated_data.get('source', instance.source)
			instance.language = validated_data.get('language', instance.language)
			instance.relation = validated_data.get('relation', instance.relation)
			instance.coverage = validated_data.get('coverage', instance.coverage)
			instance.rights = validated_data.get('rights', instance.rights)
			
			instance.save()

			return instance

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(ItemSerializer, self).get_validation_exclusions()

		return exclusions + ['creator']