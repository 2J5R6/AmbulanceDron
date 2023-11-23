# events.py

class Event:
    """Base class for events in the drone's state machine."""
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.handled = False

class LowBatteryEvent(Event):
    """Event triggered when the drone's battery level is low."""
    def __init__(self):
        super().__init__('LowBattery', "Battery level is critically low.")

class ObstacleDetectedEvent(Event):
    """Event triggered when an obstacle is detected in the drone's path."""
    def __init__(self, obstacle_type):
        super().__init__('ObstacleDetected', f"An obstacle has been detected: {obstacle_type}.")
        self.obstacle_type = obstacle_type

class GPSLostEvent(Event):
    """Event triggered when the drone's GPS signal is lost."""
    def __init__(self):
        super().__init__('GPSLost', "GPS signal has been lost.")

class HighTurbulenceEvent(Event):
    """Event triggered when high turbulence is detected during the drone's flight."""
    def __init__(self):
        super().__init__('HighTurbulence', "High turbulence detected.")

class EngineFailureEvent(Event):
    """Event triggered when a failure is detected in one of the drone's engines."""
    def __init__(self, engine_id):
        super().__init__('EngineFailure', f"Engine {engine_id} has failed.")
        self.engine_id = engine_id

class LandingSiteClearEvent(Event):
    """Event triggered when the landing site is detected to be clear."""
    def __init__(self):
        super().__init__('LandingSiteClear', "Landing site is clear.")

class LandingSiteOccupiedEvent(Event):
    """Event triggered when the landing site is detected to be occupied."""
    def __init__(self):
        super().__init__('LandingSiteOccupied', "Landing site is occupied.")

class FlightStartCommandEvent(Event):
    """Event triggered when a command to start the flight is received."""
    def __init__(self):
        super().__init__('FlightStartCommand', "Flight start command received.")

class EmergencyLocationReceivedEvent(Event):
    """Event triggered when the location of an emergency is received."""
    def __init__(self, location):
        super().__init__('EmergencyLocationReceived', "Emergency location received.")
        self.location = location

class EmergencyLocationUpdatedEvent(Event):
    """Event triggered when the emergency location is updated."""
    def __init__(self, new_location):
        super().__init__('EmergencyLocationUpdated', "Emergency location updated.")
        self.new_location = new_location

class VitalSignsDetectedEvent(Event):
    """Event triggered when the patient's vital signs are detected."""
    def __init__(self, vital_signs):
        super().__init__('VitalSignsDetected', "Patient's vital signs detected.")
        self.vital_signs = vital_signs

class ElectricalDischargeCommandEvent(Event):
    """Event triggered when a command for an electrical discharge is received."""
    def __init__(self):
        super().__init__('ElectricalDischargeCommand', "Electrical discharge command received.")
