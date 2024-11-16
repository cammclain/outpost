from __future__ import annotations
from litestar.middleware.base import AbstractMiddleware
from litestar.exceptions import PermissionDeniedException
from ..database.models.teamserver import TeamserverUser  
from ..routes.auth import AuthController  

# TODO: This middleware is not complete. It needs to be completed to check if the user is authenticated and redirect to the login page if not.

# This middleware is used to check if the user is authenticated
class AuthenticationMiddleware(AbstractMiddleware):
    async def __call__(self, scope, receive, send):
        # Create a request object from the scope
        request = scope["app"].request_class(scope, receive, send)
        # Get the session from the request
        session = request.session  # Assuming you're using session middleware
        # Get the user id from the session
        user_id = session.get("user_id")
        
        if user_id:
            # Fetch user from database
            user = await TeamserverUser.get(id=user_id)  # Adjust query based on your ORM
            # Check if the user exists
            if user:
                # Add the user to the request scope
                request.scope["user"] = user
                # Call the next middleware
                await self.app(scope, receive, send)
                # Return if the user is authenticated
                return
        
        # Redirect to login if user is not authenticated
        raise PermissionDeniedException(detail="User is not authenticated.")
