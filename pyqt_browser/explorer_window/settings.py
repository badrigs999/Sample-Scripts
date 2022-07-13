
import os
import sys
import json

sys_user = os.path.expanduser("~")
if sys.platform.startswith("win"):
    bot_browser_support_path = "%s/AppData/Roaming/DAM/bot_browser"%sys_user
elif sys.platform.startswith('lin'):
    bot_browser_support_path = "/%s/.dam/bot_browser"%sys_user
elif sys.platform.startswith('dar'):
    bot_browser_support_path = "/%s/Library/Application/Support/DAM/bot_browser"%sys_user

def get_settings_json_path():
    if not os.path.exists(bot_browser_support_path):
        os.makedirs(bot_browser_support_path)
    bot_browser_setting_path = os.path.join(bot_browser_support_path, "browser_settings.json")
    if not os.path.exists(bot_browser_setting_path):
        with open(bot_browser_setting_path, 'w') as f:
            json.dump({"app_settings": True}, f)
    return bot_browser_setting_path

def get_settings_data():
    if not os.path.exists(bot_browser_support_path):
        os.makedirs(bot_browser_support_path)
    settings_path = get_settings_json_path()
    settings_data = {}
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            settings_data = json.load(f)
    return settings_data

def set_settings_data(data):
    settings_path = get_settings_json_path()
    if os.path.exists(settings_path):
        settings_data = get_settings_data()
        with open(settings_path, "w") as f:
            settings_data.update(data)
            json.dump(settings_data, f)
        return settings_data

def load_preview_mode(mode):
    settings_data = get_settings_data()
    if settings_data:
        return settings_data.get(mode, False)
    return False

def save_preview_mode(mode, state):
    browser_settings = get_settings_json_path()
    settings_data = get_settings_data()
    settings_data.update({mode: state})
    with open(browser_settings, "w") as f:
        json.dump(settings_data, f)