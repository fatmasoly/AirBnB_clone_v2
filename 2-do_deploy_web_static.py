#!/usr/bin/python3
from time import strftime
from fabric.api import local, env, run, put
from datetime import date
import os

env.hosts = ["100.25.17.146", "54.209.46.98"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Deploy an archive to the web servers.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    try:
        if not (os.path.exists(archive_path)):
            return False

        put(archive_path, "/tmp/")

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'.format(timestamp))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception as e:
        print(e)
        return False

    return True
