#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import *
import os


env.hosts = ['3.90.84.234', '100.25.222.100']

def do_deploy(archive_path):
    """Deploying the pack to the server."""
    if not os.path.isfile(archive_path):
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        name = archive_name.split('.')[0]
        put(archive_name, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, name))
        run("rm -rf /data/web_static/releases/{}/".format(name))
        run('rm /tmp/{}'.format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* "
                "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run('rm -rf /data/web_static/current')
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))
        return True
    except:
        return False
