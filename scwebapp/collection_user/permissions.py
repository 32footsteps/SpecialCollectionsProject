from rest_framework import permissions

class IsSCUserOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, sc_user):
		if request.user:
			return sc_user == request.user

		return False