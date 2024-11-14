

# pulls everything together for the the full outpost core application

from __future__ import annotations

from litestar import Litestar


## the main application object
app = Litestar(
    route_handlers=[],
)
