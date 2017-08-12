import time

from alert_service import AlertService
from outlook_service import OutlookService


def run():
    interval = 60 * 15 # 15 minutes
    while True:
        outlook_service = OutlookService()
        unread_messages = outlook_service.get_priority_messages()
        if len(unread_messages) > 0:
            alert_service = AlertService(unread_messages)
            alert_service.push()
        time.sleep(interval)

