# coding: utf-8
import os
import json

class Video:
    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.basename = os.path.basename(self.fullpath)
        self.thumbnail_fullpath = os.path.dirname(self.fullpath) + "/" + os.path.basename(self.fullpath).split(".")[0] + ".mp4.cover.jpg"
        if not os.path.exists(self.thumbnail_fullpath):
            self.thumbnail_fullpath = os.path.dirname(self.fullpath) + "/default.png"
        self.thumbnail_basename = os.path.basename(self.thumbnail_fullpath)

    def convert_to_dict(self):
        return self.__dict__
    def to_json(self):
        return json.dumps(self, default=self.convert_to_dict)


