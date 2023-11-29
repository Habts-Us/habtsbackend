from rest_framework import permissions

class IsOwnerOrTeamMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the CollaborativeList
        # or a member of the associated Team.
        return obj.user == request.user or (obj.team and (request.user == obj.team.member1 or request.user == obj.team.member2))
    


