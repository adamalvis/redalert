import sys
import time

from alert_service import AlertService
from outlook_service import OutlookService


def run():
    minutes = float(sys.argv[1]) if len(sys.argv) > 1 else 15
    interval = 60 * minutes # 15 minutes
    while True:
        outlook_service = OutlookService()
        unread_messages = outlook_service.get_priority_messages()
        if len(unread_messages) > 0:
            alert_service = AlertService(unread_messages)
            alert_service.push()
        else:
            print('Nothing urgent atm')
        time.sleep(interval)
