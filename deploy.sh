#!/usr/bin/env bash

set -eu

container_mgmt=docker

if ! command -v docker &> /dev/null; then
    container_mgmt=podman
    if ! command -v podman &> /dev/null; then
        echo "Couldn't find docker or podman command"
        exit 1
    fi
fi

$container_mgmt build -t wherex/metrics .
$container_mgmt run --restart always -d -p 8000:8000 -e GUNICORN_CMD_ARGS="--workers=2" wherex/metrics