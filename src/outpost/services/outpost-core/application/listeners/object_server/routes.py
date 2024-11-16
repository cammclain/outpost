from __future__ import annotations

from litestar import Controller, get, post

from ...dashboard.database.models.teamserver import TeamserverBeaconObject


class ObjectServerController(Controller):
    path = "/object"

    @get()
    async def get_object(self, object_id: str, agent_id: str) -> TeamserverBeaconObject:
        # TODO: Query the seaweedfs cluster for the object data for the agent to download
        # TODO: validate the agent_id matches the agent_id in the database for the object
        # TODO: return the object data
        
        return TeamserverBeaconObject.get(object_id)

    