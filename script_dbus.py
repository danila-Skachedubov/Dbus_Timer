#!/usr/bin/env python3
from datetime import datetime
from pydbus import SessionBus
import os

os.environ.get('DBUS_SESSION_BUS_ADDRESS')
os.environ['DISPLAY'] = ':0'

bus = SessionBus()
notifications = bus.get("org.freedesktop.Notifications", # Bus name
    "/org/freedesktop/Notifications" # Object path)
)

current_time = datetime.now().strftime("%H:%M:%S")

notifications.Notify('test', 0, 'dialog-information', str(current_time) , "Текущее системное врмея", [], {}, 5000)