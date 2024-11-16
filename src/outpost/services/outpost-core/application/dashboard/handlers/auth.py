from __future__ import annotations



from litestar import Request
from litestar.exceptions import PermissionDeniedException

async def is_authenticated_guard(request: Request) -> None:
    user = request.scope.get("user")
    if not user:
        raise PermissionDeniedException(detail="User is not authenticated.")


