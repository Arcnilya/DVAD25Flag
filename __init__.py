from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import BaseFlag, get_flag_class, FLAG_CLASSES
from CTFd.models import db, Flags

class DVAD25BaseFlag(BaseFlag):
    name = "DVAD25"
    templates = {  
        "create": "/plugins/flags/assets/DVAD25/create.html",
        "update": "/plugins/flags/assets/DVAD25/edit.html",
    }

    @staticmethod
    def compare(chal_key_obj, provided):
        saved = chal_key_obj.content
        data = chal_key_obj.data
        #world = chal_key_obj.world
        #machine = chal_key_obj.machine

        if provided == saved:
            return True
        else:
            return False

'''
class DVAD25Flags(Flags):
    __tablename__ = "dvad25flags"
    id = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(
        db.Integer, db.ForeignKey("challenges.id", ondelete="CASCADE")
    )
    type = db.Column(db.String(80))
    content = db.Column(db.Text)
    data = db.Column(db.Text)
    world = db.Column(db.Text)
    machine = db.Column(db.Text)

    __mapper_args__ = {'polymorphic_identity': 'DVAD25'}

    def __init__(self, *args, **kwargs):
        super(Flags, self).__init__(**kwargs)

    def __repr__(self):
        return "<Flag {0} for challenge {1}>".format(self.content, self.challenge_id)
'''


def load(app):
    #app.db.create_all()
    FLAG_CLASSES['DVAD25'] = DVAD25BaseFlag
    register_plugin_assets_directory(app, base_path="/plugins/DVAD25Flags/assets/")
