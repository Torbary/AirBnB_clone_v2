#!/usr/bin/python3
"""Fabric script to generates a .tgz archive"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Function to generate .tgz archive from web_static folder"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)

        local("tar -cvzf {} web_static".format(file_name))
        return file_name

    except Exception:
        return None
