# app/spatial_logic1.py

from dataclasses import dataclass
from typing import List, Tuple
import math

@dataclass
class Device:
    id: str
    x: float
    y: float
    signal_radius: float

    def distance_to(self, other: 'Device') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def check_connections(devices: List[Device]) -> List[Tuple[str, str, str]]:
    connections = []
    for i, d1 in enumerate(devices):
        for j in range(i + 1, len(devices)):
            d2 = devices[j]
            dist = d1.distance_to(d2)

            if dist <= min(d1.signal_radius, d2.signal_radius):
                status = "interfering"
            elif dist <= d1.signal_radius or dist <= d2.signal_radius:
                status = "connected"
            elif dist <= (d1.signal_radius + d2.signal_radius):
                status = "overlapping"
            else:
                continue  # too far
            connections.append((d1.id, d2.id, status))
    return connections
