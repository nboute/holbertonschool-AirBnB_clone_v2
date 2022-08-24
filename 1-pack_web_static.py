#!/usr/bin/python3

from fabric.operations import local
from datetime import datetime


def do_pack():
    filename = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(filename))
    if result.failed is True:
        return None
    else:
        return filename
