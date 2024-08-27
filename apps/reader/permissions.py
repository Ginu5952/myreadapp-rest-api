# TODO: Create a custom permission that will make sure that
# it checks the authenticated user id is the same as the reader user id.

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# IsAuthenticated -> If user is not authenticated, it will fail
# IsAdminUser -> `is_staff` is `False`, it will fail
# IsAuthenticatedOrReadOnly -> CRUD
    # POST
    # GET        -> Read, no authentication needed
    # PUT, PATCH
    # DELETE