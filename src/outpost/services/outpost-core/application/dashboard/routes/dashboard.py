from __future__ import annotations

from litestar import Controller, get, post
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

## import the models
from ...dashboard.database.models.teamserver import TeamserverAgent, TeamserverBeaconObject, TeamserverCampaign, TeamserverListener, TeamserverTask, TeamserverTarget, TeamserverTargetGroup
from litestar.response import Template
from litestar.di import Provide
from ..handlers.auth import is_authenticated_guard

class DashboardController(Controller):
    path = "/dashboard" 
    guards = [is_authenticated_guard]
    @get()
    async def get_dashboard(self, db_session: AsyncSession) -> Template:
        # Get counts of various entities
        campaign_count = await db_session.scalar(
            select(func.count()).select_from(TeamserverCampaign)
        )
        agent_count = await db_session.scalar(
            select(func.count()).select_from(TeamserverAgent)
        )
        target_count = await db_session.scalar(
            select(func.count()).select_from(TeamserverTarget)
        )
        listener_count = await db_session.scalar(
            select(func.count()).select_from(TeamserverListener)
        )
        task_count = await db_session.scalar(
            select(func.count()).select_from(TeamserverTask)
        )

        return Template(
            template_name="views/dashboard/dashboard.html",
            context={
                "campaign_count": campaign_count,
                "agent_count": agent_count,
                "target_count": target_count,
                "listener_count": listener_count,
                "task_count": task_count
            }
        )

    class Campaigns(Controller):
        path = "/campaigns"
        guards = [is_authenticated_guard]
        @get()
        async def get_campaigns(self, db_session: AsyncSession) -> Template:
            # Get all campaigns with related data
            campaigns = await db_session.execute(
                select(TeamserverCampaign)
            )
            campaigns = campaigns.scalars().all()

            # Get summary counts for each campaign
            campaign_data = []
            for campaign in campaigns:
                target_count = len(campaign.targets)
                agent_count = len(campaign.agents)
                task_count = sum(len(agent.tasks) for agent in campaign.agents)
                
                campaign_data.append({
                    "campaign": campaign,
                    "target_count": target_count,
                    "agent_count": agent_count,
                    "task_count": task_count
                })

            return Template(
                template_name="views/dashboard/campaigns.html",
                context={"campaigns": campaign_data}
            )

    class Targets(Controller):
        path = "/targets"
        guards = [is_authenticated_guard]
        @get()
        async def get_targets(self, db_session: AsyncSession) -> Template:
            # Get all targets with related data
            targets = await db_session.execute(
                select(TeamserverTarget)
            )
            targets = targets.scalars().all()

            target_data = []
            for target in targets:
                agent_count = len(target.agents)
                task_count = sum(len(agent.tasks) for agent in target.agents)
                
                target_data.append({
                    "target": target,
                    "agent_count": agent_count,
                    "task_count": task_count
                })

            return Template(
                template_name="views/dashboard/targets.html",
                context={"targets": target_data}
            )

    class Listeners(Controller):
        path = "/listeners"
        guards = [is_authenticated_guard]
        @get()
        async def get_listeners(self, db_session: AsyncSession) -> Template:
            # Get all listeners with related data
            listeners = await db_session.execute(
                select(TeamserverListener)
            )
            listeners = listeners.scalars().all()

            listener_data = []
            for listener in listeners:
                agent_count = len(listener.agents)
                task_count = sum(len(agent.tasks) for agent in listener.agents)
                
                listener_data.append({
                    "listener": listener,
                    "agent_count": agent_count,
                    "task_count": task_count
                })

            return Template(
                template_name="views/dashboard/listeners.html",
                context={"listeners": listener_data}
            )

    class Agents(Controller):
        path = "/agents"

        @get()
        async def get_agents(self, db_session: AsyncSession) -> Template:
            # Get all agents with related data
            agents = await db_session.execute(
                select(TeamserverAgent)
            )
            agents = agents.scalars().all()

            agent_data = []
            for agent in agents:
                task_count = len(agent.tasks)
                
                agent_data.append({
                    "agent": agent,
                    "task_count": task_count,
                    "listener": agent.listener
                })

            return Template(
                template_name="views/dashboard/agents.html",
                context={"agents": agent_data}
            )

    class Tasks(Controller):
        path = "/tasks"

        @get()
        async def get_tasks(self, db_session: AsyncSession) -> Template:
            # Get all tasks with related data
            tasks = await db_session.execute(
                select(TeamserverTask)
            )
            tasks = tasks.scalars().all()

            task_data: list[dict] = []
            for task in tasks:
                task_data.append({
                    "task": task,
                    "agent": task.agent,
                    "listener": task.agent.listener
                })

            return Template(
                template_name="views/dashboard/tasks.html",
                context={"tasks": task_data}
            )

    class Beacons(Controller):
        path = "/beacons"

        @get()
        async def get_beacons(self, db_session: AsyncSession) -> Template:
            # Get all beacons with related data
            beacons = await db_session.execute(
                select(TeamserverBeaconObject)
            )
            beacons = beacons.scalars().all()

            beacon_data: list[dict] = []
            for beacon in beacons:
                beacon_data.append({
                    "beacon": beacon,
                    "agent": beacon.agent,
                    "listener": beacon.agent.listener
                })

            return Template(
                template_name="views/dashboard/beacons.html",
                context={"beacons": beacon_data}
            )
