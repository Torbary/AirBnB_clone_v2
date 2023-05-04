#!/usr/bin/python3
"""
Fabric script to deploy an archive to my web servers
"""

import os
from fabric.api import env, put, run

env.hosts = ["34.207.211.110", "54.152.234.206"]


def do_deploy(archive_path):
    """Distibutes an archive to the servers"""
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    directory = "/data/web_static/releases/{}".format(filename.split(".")[0])

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(directory))
        run("tar -xzf /tmp/{} -C {}/".format(filename, directory))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(directory, directory))
        run("rm -rf {}/web_static".format(directory))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(directory))
        print("New version deployed!")
        return True
    except ValueError:
        return False
