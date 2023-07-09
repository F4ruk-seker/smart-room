from esp import sensor_permissions
from esp import sensor_actions
from .base_sensor import SensorBase


class MotionSensor(SensorBase):
    action_classes = [
        sensor_actions.OpenCurrent
    ]

    permission_classes = [
        sensor_permissions.TimeRange
    ]


