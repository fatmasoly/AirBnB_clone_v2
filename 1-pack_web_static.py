#!/usr/bin/python3

"""
This script creates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repository.
"""

from time import strftime
from fabric.api import local
from datetime import date


def do_pack():
    """
    Creates a .tgz archive with a unique filename based on the current
    timestamp and stores it in the versions folder.

    Returns:
        str: The path of the generated archive if successful, None otherwise.
    """
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))
        return "versions/web_static_{}.tgz".format(filename)
    except Exception as a:
        return None
