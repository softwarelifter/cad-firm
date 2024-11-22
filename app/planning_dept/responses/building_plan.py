from typing import List, Literal
from pydantic import BaseModel


class Door(BaseModel):
    door_type: str
    length: float
    location: str


class Bathroom(BaseModel):
    bathroom_type: str
    label: str
    length: float
    width: float
    area: float
    door: Door


class Room(BaseModel):
    room_type: str
    label: str
    length: float
    width: float
    area: float
    doors: List[Door]
    bathroom: Bathroom


class BuildingPlan(BaseModel):
    address: str
    building_type: str
    floors: int
    length: float
    width: float
    """assuming the plot is rectangular in shape,"""
    area: float
    total_builtup_area: float
    owner: str
    architect: str
    contractor: str
    status: str
    rooms: List[Room]  # Use List from typing
