from __future__ import annotations

from litestar import Controller, get, post




## import the models
from ...dashboard.database.models.teamserver import TeamserverAgent, TeamserverBeaconObject, TeamserverCampaign, TeamserverListener, TeamserverTask, TeamserverTarget, TeamserverTargetGroup



class DashboardController(Controller):
    path = "/dashboard"

    @get()
    async def get_dashboard(self) -> JinjaTemplate:
        return JinjaTemplate("dashboard.html")
