from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import BaseFlag, get_flag_class, FLAG_CLASSES
from CTFd.models import db, Flags
from datetime import datetime
from hashlib import sha1

class DVAD25BaseFlag(BaseFlag):
    name = "DVAD25"
    templates = {  
        "create": "/plugins/DVAD25Flag/assets/DVAD25/create.html",
        "update": "/plugins/DVAD25Flag/assets/DVAD25/edit.html",
    }

    @staticmethod
    def compare(chal_key_obj, provided):
        dt = datetime.now()
        today = dt.strftime('%d%m%Y')
        saved = chal_key_obj.content
        #print("flag content:", saved)
        data = chal_key_obj.data
        #print("flag data:", data)
        world, machine = data.split('+')
        secret = "1337"

        flag_info = f"{saved}{world}{machine}{today}{secret}"
        print("flag_info:", flag_info)
        flag_hash = sha1(flag_info.encode())
        calculated_flag = "flag{"+saved+flag_hash"}"
        print("calc_flag:", calculated_flag)

        if provided == calculated_flag:
            return True
        else:
            return False


def load(app):
    FLAG_CLASSES['DVAD25'] = DVAD25BaseFlag
    register_plugin_assets_directory(app, base_path="/plugins/DVAD25Flag/assets/")
