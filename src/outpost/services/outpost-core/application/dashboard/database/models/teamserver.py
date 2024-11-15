# this file contains the models for the teamserver

from __future__ import annotations


from ..db import base

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Teamserver(base):
    __tablename__ = "teamservers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Teamserver(name='{self.name}', url='{self.url}', is_active={self.is_active})>"


# this is a user that has access to the teamserver
class TeamserverUser(base):
    __tablename__ = "teamserver_users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    teamserver_id = Column(Integer, ForeignKey("teamservers.id"))
    teamserver = relationship("Teamserver", back_populates="users")

# this is a campaign that is running on the teamserver.
# campagins have agents, tasks, and targets as the main components.
# for metadata about the campaign, we will use the TeamserverCampaign model.
class TeamserverCampaign(base):
    __tablename__ = "teamserver_campaigns"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teamserver_id = Column(Integer, ForeignKey("teamservers.id"))
    teamserver = relationship("Teamserver", back_populates="campaigns")
    description = Column(String, nullable=True)

    # the agents that are associated with a target in the campaign
    agents = relationship("TeamserverAgent", back_populates="campaign")
    # the targets that are associated with a target group in the campaign
    targets = relationship("TeamserverTarget", back_populates="campaign")
    # the target groups that are associated with the campaign
    target_groups = relationship("TeamserverTargetGroup", back_populates="campaign")
    # the tasks that are associated with the campaign
    tasks = relationship("TeamserverTask", back_populates="campaign")
    # the listeners that are associated with the campaign
    listeners = relationship("TeamserverListener", back_populates="campaign")

    def __repr__(self):
        return f"<TeamserverCampaign(name='{self.name}', teamserver_id='{self.teamserver_id}')>"


class TeamserverAgent(base):
    __tablename__ = "teamserver_agents"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    registration_key = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # the target that the agent is assigned to
    target_id = Column(Integer, ForeignKey("targets.id"))
    target = relationship("Target", back_populates="agents")
    # the teamserver that the agent is running on
    teamserver_id = Column(Integer, ForeignKey("teamservers.id"))
    teamserver = relationship("Teamserver", back_populates="agents")
    # the campaign that the agent is running on
    campaign_id = Column(Integer, ForeignKey("teamserver_campaigns.id"))
    campaign = relationship("TeamserverCampaign", back_populates="agents")


class TeamserverTask(base):
    __tablename__ = "teamserver_tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    command = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
    # the agent that the task is assigned to
    agent_id = Column(Integer, ForeignKey("teamserver_agents.id"))
    agent = relationship("TeamserverAgent", back_populates="tasks")



class TeamserverTarget(base):
    __tablename__ = "teamserver_targets"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # the group that the target belongs to
    group_id = Column(Integer, ForeignKey("teamserver_target_groups.id"))
    group = relationship("TeamserverTargetGroup", back_populates="targets")


# this is a group of targets that are related to each other in the same campaign.
# a campaign can have many target groups.
class TeamserverTargetGroup(base):
    __tablename__ = "teamserver_target_groups"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    targets = relationship("TeamserverTarget", back_populates="group")

# this is a listener that is running on the teamserver or routing traffic to the teamserver as it's destination.
class TeamserverListener(base):
    __tablename__ = "teamserver_listeners"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teamserver_id = Column(Integer, ForeignKey("teamservers.id"))
    teamserver = relationship("Teamserver", back_populates="listeners")
    # the type of listener
    listener_type = Column(String, nullable=False)
    # the port that the listener is listening on
    port = Column(Integer, nullable=False)
    # the address that the listener is listening on
    listener_address = Column(String, nullable=False)
    # the public address that the listener is exposed on
    public_address = Column(String, nullable=False)
    # the public port that the listener is exposed on
    public_port = Column(Integer, nullable=False)


## Team Server Objects in the "arsenal" to be served up to the beacons
class TeamserverObject(base):
    __tablename__ = "teamserver_objects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    object_data = Column(String)
    compatible_agents = Column(String)
    # the url location of the object in the seaweedfs cluster
    seaweedfs_url_location = Column(String)
## Team Server Beacon Objects that are being actively deployed to the beacons
# This is an object that is served up to the beacon to be executed by the beacon.
class TeamserverBeaconObject(TeamserverObject):
    __tablename__ = "teamserver_beacon_objects"
    id = Column(Integer, primary_key=True)
    #  the campaign that the beacon object is associated with
    campaign_id = Column(Integer, ForeignKey("teamserver_campaigns.id"))
    campaign = relationship("TeamserverCampaign", back_populates="beacon_objects")
    # the teamserver that the beacon object is associated with
    teamserver_id = Column(Integer, ForeignKey("teamservers.id"))
    teamserver = relationship("Teamserver", back_populates="beacon_objects")
    
