from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from collection.models import SCUser

class SCUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)


	class Meta:
			model = SCUser
			fields = ('id', 'email', 'username', 'first_name', 'last_name', 'created_at', 'updated_at',
				'password', 'confirm_password',)

			read_only_fields = ('created_at', 'updated_at',)

			def create(self, validated_data):
				return SCUser.objects.create(**validated_data)

			def update(self, instance, validated_data):
				instance.username = validated_data.get('username', instance.username)
				instance.first_name = validated_data.get('firstname', instance.first_name)
				instance.last_name = validated_data.get('lastname', instance.last_name)
				instance.email = validated_data.get('email', instance.email)

				instance.save()

				password = validated_data.get('password', None)
				confirm_password= validated_data.get('confirm_password', None)

				if password and confirm_password and password == confirm_password:
					instance.set_password(password)
					instance.save()

				update_session_auth_hash(self.context.get('request'), instance)

				return instance