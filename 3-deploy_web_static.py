#!/usr/bin/python3
"""Fabric script that creates and distrubutes an archive to web servers"""

from fabric.api import env, put, run
from os.path import exists, basename
env.hosts = ["34.207.211.110", "54.152.234.206"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """create a compressed archive of web_static contents"""
    try:
        from fabric.api import local
        from datetime import datetime
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(current_time))
        return file_name
    except ValueError:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    file_name = basename(archive_path)
    path_no_ext = "/data/web_static/releases/" + file_name[:-4]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}"
            .format(file_name, path_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(path_no_ext, path_no_ext))
        run("rm -rf {}/web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_ext))
        return True
    except ValueError:
        return False


def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
