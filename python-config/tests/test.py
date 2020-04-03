import os
import json
import configparser


ENV = os.getenv("TEST_ENV", "dev")


def print_init_config(parser):
    for section_name in parser.sections():
        print('Section:', section_name)
        for name, value in parser.items(section_name):
            print('  {} = {}'.format(name, value))
            print()


def print_json_config(data):
    print(json.dumps(data, sort_keys=True, indent=4))
    print()


def setUpRun(self):
    # INI CONFIG
    parser = configparser.ConfigParser()
    parser.read("config/config.ini")
    print("INI CONFIG:\n")
    print_init_config(parser)

    # JSON CONFIG
    with open("config/config.json") as fp:
        data = json.load(fp)

    print("JSON CONFIG:\n")
    print_json_config(data)

    print("INI URL: ", data[ENV]["url"])
    print("JSON URL: ", parser[ENV]["url"])


class ConfigModel:

    def v_state_a(self):
        pass

    def v_state_b(self):
        pass

    def v_state_c(self):
        pass

    def e_action_a(self):
        pass

    def e_action_b(self):
        pass

    def e_action_c(self):
        pass
