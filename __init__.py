from os.path import basename, dirname, join
from mycroft.skills.core import intent_file_handler, MycroftSkill
from mock_mycroft_backend import start_backend
from mock_mycroft_backend.configuration import CONFIGURATION
from mycroft.util import create_daemon
from jarbas_utils.configuration import update_mycroft_config
from mycroft.messagebus.message import Message


class MockBackendSkill(MycroftSkill):
    def __init__(self):
        super(MockBackendSkill, self).__init__(name='MockBackendSkill')
        self.reload_skill = False
        self.namespace = "jarbas.mock_backend"
        self.skill_name = "Mock Backend"
        self.backend_port = CONFIGURATION["backend_port"]
        if "use_mock" not in self.settings:
            self.settings["use_mock"] = True
            self.enable_mock(False)
        self.backend = None
        self.make_priority(False)

    def initialize(self):
        self.backend = create_daemon(start_backend)

    def get_intro_message(self):
        # welcome dialog on skill install
        self.speak_dialog("intro", {"skill_name": self.skill_name}, wait=True)
        self.speak_dialog("need_reboot")

    # config
    def make_priority(self, send_event=True):
        skill_folder = basename(dirname(__file__))
        priority_skills = self.config_core["skills"]["priority_skills"]
        if skill_folder not in priority_skills:
            priority_skills.append(skill_folder)
            config = {
                "skills": {
                    "priority_skills": priority_skills
                }
            }
            update_mycroft_config(config)
            if send_event:
                self.bus.emit(Message("configuration.updated"))

    def enable_mycroft(self, send_event=True):
        config = {
            "server": {
                "url": "https://api.mycroft.ai",
                "version": "v1"
            },
            "tts": {
                "mimic2": {
                    "url": "https://mimic-api.mycroft.ai/synthesize?text="
                }
            }
        }
        update_mycroft_config(config)
        self.settings["use_mock"] = False
        if send_event:
            self.bus.emit(Message("configuration.updated"))

    def enable_mock(self, send_event=True):
        url = "http://0.0.0.0:{p}".format(p=CONFIGURATION["backend_port"])
        version = CONFIGURATION["api_version"]
        mimic_url = "http://0.0.0.0:{p}/synthesize/mimic2/kusal/en?text=".format(p=CONFIGURATION["backend_port"])
        config = {
            "server": {
                "url": url,
                "version": version
            },
            "tts": {
                "mimic2": {
                    "url": mimic_url
                }
            }
        }
        update_mycroft_config(config)
        self.settings["use_mock"] = True
        if send_event:
            self.bus.emit(Message("configuration.updated"))

    # intents
    @intent_file_handler("enable_mycroft.intent")
    def handle_enable_mycroft(self, message):
        if self.settings["use_mock"]:
            self.gui["use_mock"] = False
            self.settings["use_mock"] = False
            self.enable_mycroft()
            self.speak_dialog("mycroft_backend", wait=True)
            self.speak_dialog("need_reboot")
        else:
            self.speak_dialog("mycroft_backend")

    @intent_file_handler("enable_mock.intent")
    def handle_enable_mock(self, message):
        if not self.settings["use_mock"]:
            self.gui["use_mock"] = True
            self.settings["use_mock"] = True
            self.enable_mock()
            self.gui.show_image(join(dirname(__file__), "logo.png"))
            self.speak_dialog("mock_backend", wait=True)
            self.speak_dialog("need_reboot")
        else:
            self.speak_dialog("mock_backend", wait=True)

    @intent_file_handler("current_backend.intent")
    def handle_current_backend(self, message):
        if self.settings["use_mock"]:
            self.speak_dialog("mock_backend")
        else:
            self.speak_dialog("mycroft_backend")

    # shutdown
    def shutdown(self):
        super(MockBackendSkill, self).shutdown()
        if self.backend is not None:
            self.backend.join(0)


def create_skill():
    return MockBackendSkill()


