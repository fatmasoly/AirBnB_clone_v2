#!/usr/bin/python3
from datetime import datetime
from fabric.api import env, local, put, run
import os.path

env.hosts = ["100.25.17.146", "54.209.46.98"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path to the created archive if successful, None otherwise."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """  Distributes an archive to your web servers, unpacks it, and sets up a
    symbolic link to the new version.

    Args:
        archive_path (str): The path to the archive file to deploy.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Creates a compressed archive of the web_static directory, deploys it to
    the web servers, and sets up a symbolic link to the new version.
    """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
