#!/usr/bin/python3

import os.path
from fabric.api import env, put, run

env.hosts = ["34.207.211.110", "54.152.234.206"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    name = os.path.splitext(archive_name)[0]

    if put(archive_path, f"/tmp/{archive_name}").failed:
        return False

    if run(f"rm -rf /data/web_static/releases/{name}/").failed:
        return False

    if run(f"mkdir -p /data/web_static/releases/{name}/").failed:
        return False

    if run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{name}/").failed:
        return False

    if run(f"rm /tmp/{archive_name}").failed:
        return False

    if run(f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/").failed:
        return False

    if run(f"rm -rf /data/web_static/releases/{name}/web_static").failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current").failed:
        return False

    return True
