from config import outlook_email, outlook_password
import outlook
from priority_checker import is_high_priority


class OutlookService(object):

    def __init__(self):
        mail = outlook.Outlook()
        mail.login(outlook_email, outlook_password)
        mail.readOnly('Inbox')
        self.mail = mail

    def get_priority_messages(self):
        unread_ids = self.mail.unreadIdsToday()
        priority_messages = []
        for unread_id in unread_ids:
            self.mail.getEmail(unread_id)
            subject = self.mail.mailsubject()
            if is_high_priority(subject):
                priority_messages.append(subject)
        return priority_messages
