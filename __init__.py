from CTFd.plugins import register_plugin_assets_directory


class FlagException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BaseFlag(object):
    name = None
    templates = {}

    @staticmethod
    def compare(self, saved, provided):
        return True


class CTFdDVAD25Flag(BaseFlag):
    name = "DVAD25"
    templates = {  
        "create": "/plugins/DVAD25Flag/assets/DVAD25/create.html",
        "update": "/plugins/DVAD25Flag/assets/DVAD25/edit.html",
    }

    @staticmethod
    def compare(chal_key_obj, provided):
        saved = chal_key_obj.content
        #data = chal_key_obj.data
        world = chal_key_obj.world

        return True
        '''
        if len(saved) != len(provided):
            return False
        result = 0

        if data == "case_insensitive":
            for x, y in zip(saved.lower(), provided.lower()):
                result |= ord(x) ^ ord(y)
        else:
            for x, y in zip(saved, provided):
                result |= ord(x) ^ ord(y)
        return result == 0
        '''


FLAG_CLASSES = {"DVAD25": CTFdDVAD25Flag}


def get_flag_class(class_id):
    cls = FLAG_CLASSES.get(class_id)
    if cls is None:
        raise KeyError
    return cls


def load(app):
    register_plugin_assets_directory(app, base_path="/plugins/DVAD25Flag/assets/")
