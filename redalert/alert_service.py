import os


class AlertService(object):
    alert_title = 'HIGH PRIORITY EMAIL'

    def __init__(self, email_subjects):
        self.email_subjects = email_subjects

    def push(self):
        for subject in self.email_subjects:
            os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Blow.aiff"'
              """.format(subject, self.alert_title))
