import uuid
from Model.EventType import EventType


class Event:
    def __init__(self, publisher, event_type:EventType, description, creation_time):
        self.description = description
        self.id = str(uuid.uuid4())
        self.publisher = publisher
        self.event_type = event_type
        self.creation_time = creation_time

    def get_id(self):
        return self.id

    def get_publisher(self):
        return self.publisher

    def get_event_type(self):
        return self.event_type

    def get_creation_time(self):
        return self.creation_time

    def get_description(self):
        return self.description
