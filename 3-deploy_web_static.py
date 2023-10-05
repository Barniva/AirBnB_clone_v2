#!/usr/bin/python3
"""This python script uploads file to a remote server"""
from os.path import exists
from fabric.api import run, put, env, local
from datetime import datetime

env.hosts = ['107.21.41.16', '3.85.16.254']


def do_pack():
    """A method that acomplishes the above objective"""
    now = datetime.now()
    appended_name = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_" + appended_name + ".tgz"

    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None

    return archive_name


def do_deploy(archive_path):
    """Deployes the archive to the webserver"""
    if not exists(archive_path):
        return False

    full_name = archive_path.split("/")[1]
    file_name = archive_path.split("/")[1].split(".")[0]

    if put(archive_path, "/tmp/{}".format(
           full_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
           full_name, file_name)).succeeded is False:
        return False

    if run("rm /tmp/{}".format(full_name)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_name, file_name)
           ).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).succeeded is False:
        return False

    return True


def deploy():
    """Deployes the static content by calling the above methods"""
    file_path = do_pack()
    if file_path is not None:
        return do_deploy(file_path)
    return False
