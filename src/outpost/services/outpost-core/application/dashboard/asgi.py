

# pulls everything together for the the full outpost core application

from __future__ import annotations
from pathlib import Path
from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
## the main application object
app = Litestar(
    route_handlers=[],
    template_config=TemplateConfig(
        engine=JinjaTemplateEngine(),
        directory=Path("templates"),
    ),
    
)
