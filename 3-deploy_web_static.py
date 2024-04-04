#!/usr/bin/python3
"""This Fabric script creates and distributes an archive to
   web servers, using the function deploy"""

import os
from fabric.api import *

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Creates a compressed archive of the web_static directory, deploys it to
    the web servers, and sets up a symbolic link to the new version."""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
