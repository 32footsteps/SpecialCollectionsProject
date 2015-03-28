from rest_framework import permissions

class IsAuthorOfCollection(permissions.BasePermission):
	def has_object_permission(self, request, view, collection):
		if request.user:
			return collection.author == request.user

		return False