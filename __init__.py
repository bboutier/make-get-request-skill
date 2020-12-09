import requests
from os.path import join

from mycroft import MycroftSkill, intent_handler


class MakeGetRequest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.settings_change_callback = self.check_settings

    def check_settings(self):
        """Check if minimum required Skill settings are available."""
        self.url = self.settings.get('url')
        self.enable_intent('make.request.intent')

    @intent_handler('make.request.intent')
    def handle_request(self, message):
        """Make the actual GET request."""
        params = {}
        params['query'] = message.data.get('utterance');

        try:
            req_response = requests.get(self.settings.get('url'), params=params)
            self.speak(req_response.text)
        except:
            self.speak_dialog('error')


def create_skill():
    return MakeGetRequest()

