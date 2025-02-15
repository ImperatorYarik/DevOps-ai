from flask import Blueprint, render_template, Response
from src.models import User
import time
import os
import docker

client = docker.from_env()

container = client.containers.get("DevOps-ai-nexus")

home_bp = Blueprint('home', __name__)


def generate_logs():
    """Simulate log generation. In real app, you might tail a real log file."""
    with open('/var/log/syslog') as f:
        f.seek(0, 2)  # Go to the end of the file
        while True:
            line = f.readline()
            if not line:
                # time.sleep(0.1)  # Wait briefly for new logs
                continue
            yield f"data: {line.strip()}\n\n"
    # log_lines = [
    #     "INFO: Server started successfully",
    #     "DEBUG: Loading configuration",
    #     "INFO: Database connection established",
    #     "WARNING: High memory usage detected",
    #     "ERROR: Failed to process request",
    #     "INFO: Cache cleared successfully",
    #     "DEBUG: Running background tasks"
    # ]
    #
    # while True:
    #     # Simulate new log entry
    #     log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {log_lines[int(time.time()) % len(log_lines)]}"
    #     yield f"data: {log_entry}\n\n"
    #     time.sleep(2)

@home_bp.route('/')
def home():
    message = User.get_welcome_message()
    return render_template('home.html', message=message)

@home_bp.route('/stream-logs')
def stream_logs():
    return Response(generate_logs(), mimetype='text/event-stream')

