#!/usr/bin/python3

from fabric.operations import local
from fabric.operations import put
from fabric.operations import run
from fabric.api import env
from fabric.api import hosts
import fabric
from datetime import datetime
import os


def do_pack():
    """Pack web_static folder for future deployment"""
    filename = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(filename))
    if result.failed is True:
        return None
    else:
        return filename


env.hosts = ['54.167.41.249', '54.160.234.222']


def do_deploy(archive_path):
    """Deploy given archive to web server"""
    if os.path.exists(archive_path) is False:
        return False
    result = put(archive_path, '/tmp/')
    if result.failed is True:
        return False
    filename = os.path.basename(archive_path)
    result = run("mkdir -p /data/web_static/releases/{}".format(filename[:-4]))
    if result.failed is True:
        return False
    result = run(("tar -xf /tmp/" +
                  "{} -C /data/web_static/releases/{}" +
                  " --strip-components=1").format(filename, filename[:-4]))
    if result.failed is True:
        return False
    result = run("rm /tmp/{}".format(filename))
    if result.failed is True:
        return False
    result = run("rm /data/web_static/current")
    if result.failed is True:
        return False
    result = run("ln -s /data/web_static/releases/"
                 "{} /data/web_static/current".format(filename[:-4]))
    if result.failed is True:
        return False
    print("New version deployed!")
    return True
