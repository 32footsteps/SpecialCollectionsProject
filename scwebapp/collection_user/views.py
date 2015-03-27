import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from django.template import loader
from django.http import HttpResponse
from collection_user.models import SCUser
from collection_user.serializers import SCUserSerializer

class SCUserViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = SCUser.objects.all()
	serializer_class = SCUserSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == "POST":
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		print("serializer data: " + str(request.data))
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			SCUser.objects.create_user(**serializer.validated_data)

			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

		print(str(serializer.errors))
	
		return Response({
			'status': 'Bad Request',
			'message': 'Account could not be created'
			}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
	def post(self, request, format=None):
		data = json.loads(request.body.decode('utf-8'))

		username = data.get('username', None)
		password = data.get('password', None)

		account = authenticate(username=username, password=password)

		if account is not None:
			if account:
				login(request, account)
				serialized = SCUserSerializer(account)
				return Response(serialized.data)
			else:
				return Response({
				'status': 'Unauthorized',
				'message': 'This account has been disabled.'

				}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({
				'status': 'Unauthorized',
				'message': 'Username/password combination is invalid.'

			}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request, format=None):
		logout(request)

		return Response({}, status=status.HTTP_204_NO_CONTENT)

def dash(request):
	template = loader.get_template('index.html')
	return HttpResponse(template)