#!/usr/bin/env python3
from datetime import datetime
from pydbus import SessionBus

bus = SessionBus()
notifications = bus.get("org.freedesktop.Notifications", # Bus name
    "/org/freedesktop/Notifications" # Object path)
)

current_time = datetime.now().strftime("%H:%M:%S")

notifications.Notify('test', 0, 'dialog-information', str(current_time) , "Текущее системное врмея", [], {}, 5000)