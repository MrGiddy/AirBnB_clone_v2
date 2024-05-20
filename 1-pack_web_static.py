#!/usr/bin/python3
"""Defines a script that generates a .tgz archive from web_static folder"""
from fabric.api import task
from datetime import datetime, timezone
from fabric.api import local


@task
def do_pack():
    """Generates a compressed archive(.tgz) from web_static folder"""
    local('mkdir -p versions')

    ts = datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')
    file = f'versions/web_static_{ts}.tgz'
    res = local(f'tar -cvzf {file} -C web_static .')

    if res.failed:
        return None
    return file
