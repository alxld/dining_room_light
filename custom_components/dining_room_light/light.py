"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = DiningRoomLight()
    add_entities([ent])


class DiningRoomLight(NewLight):
    """Dining Room Light."""

    def __init__(self) -> None:
        """Initialize Dining Room Light."""
        super(DiningRoomLight, self).__init__(
            "Dining Room", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.dining_room_chandeliers_group"] = None
        self.entities["light.dining_room_group"] = None
        self.switch = "Dining Room Switch"
        self.motion_sensors.append("Dining Room Motion Sensor")
        self.has_brightness_threshold = True
        self.brightness_threshold = 128
        self.motion_sensor_brightness = 128
