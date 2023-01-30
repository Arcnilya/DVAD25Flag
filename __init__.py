from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import BaseFlag, get_flag_class, FLAG_CLASSES
from CTFd.models import db, Flags

class DVAD25BaseFlag(BaseFlag):
    name = "DVAD25"
    templates = {  
        "create": "/plugins/DVAD25Flags/assets/DVAD25/create.html",
        "update": "/plugins/DVAD25Flags/assets/DVAD25/edit.html",
    }

    @staticmethod
    def compare(chal_key_obj, provided):
        saved = chal_key_obj.content
        data = chal_key_obj.data
        print("flag content:", saved)
        print("flag data:", data)

        if provided == saved:
            return True
        else:
            return False


def load(app):
    FLAG_CLASSES['DVAD25'] = DVAD25BaseFlag
    register_plugin_assets_directory(app, base_path="/plugins/DVAD25Flags/assets/")
