from __future__ import annotations

from litestar import Controller, get, post

from ...dashboard.database.models.teamserver import TeamserverAgent, TeamserverTask, TeamserverTarget