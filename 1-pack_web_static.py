#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """defining the do_pack module"""
    if not os.path.exists("./versions/"):
        local("mkdir ./versions/")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_{}.tgz'.format(time)
    result = local('tar -cvzf {} web_static'.format(path))
    return path
