class SettingsCloud:
    settings = dict()

    @staticmethod
    def setParameter(key, value):
        SettingsCloud.settings[key] = value

    @staticmethod
    def getParameter(key):
        if key not in SettingsCloud.settings:
            return None
        return SettingsCloud.settings[key]

    @staticmethod
    def resetSettings():
        SettingsCloud.settings.clear()