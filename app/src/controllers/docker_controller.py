from pyexpat.errors import messages

from flask import Blueprint, render_template, Response

import docker


docker_bp = Blueprint('docker', __name__)

@docker_bp.route('/docker')
def home():
    client = docker.from_env()
    info = client.info()

    parsed_info = {
        "Containers": info.get("Containers"),
        "Running Containers": info.get("ContainersRunning"),
        "Paused Containers": info.get("ContainersPaused"),
        "Stopped Containers": info.get("ContainersStopped"),
        "Images": info.get("Images"),
        "Operating System": info.get("OperatingSystem"),
        "Kernel Version": info.get("KernelVersion"),
        "Docker Version": info.get("ServerVersion"),
        "Storage Driver": info.get("Driver"),
        "Total Memory (GB)": round(info.get("MemTotal", 0) / (1024 ** 3), 2),
        "CPUs": info.get("NCPU"),
    }

    return render_template('docker/index.html', message=parsed_info)

@docker_bp.route("/docker/containers")
def containers():
    client = docker.from_env()

    containers = [
        {
            "ID": container.id,
            "Name": container.name,
            "Image": container.image.tags,
            "Status": container.status
        }
        for container in client.containers.list()
    ]
