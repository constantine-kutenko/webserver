# webserver

## Table of Contents

* [Overview](#overview)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [Dependencies](#dependencies)
* [Usage](#usage)
* [Building and running image](#building-and-running-image)
* [Environment variables](#environment-variables)

## Overview

A fairly simple HTTP server written in Python 3 and can be run as a standalone script or within a container.

## Purpose

This application is meant for debugging purposes as well as a template for further development.

## Requirements

* Python 3.x
* Python `HTTPServer` module
* Docker (of any version) in case running in container

## Dependencies

The only dependency can be fulfilled with the following command:

```bash
pip3 install HTTPServer
```

Alternatively `pip3 install -r requirements.txt` can be issued.

## Usage

Run the application:

```bash
LISTEN_ADDR=127.0.0.1 \
    LISTEN_PORT=5000 \
    LOG_LEVEL=debug \
    python3 app/app.py
```

## Building and running image

To build an image run following command in repository root path:

```bash
docker build \
    --pull \
    --tag webserver:0.0.1 \
    -f docker/Dockerfile .
```

To run the image (with defaults) use:

```bash
docker run \
    --rm \
    --name webserver \
    --hostname webserver \
    --publish 5000:5000 \
    -e LISTEN_ADDR=127.0.0.1 \
    -e LISTEN_PORT=5000 \
    -e LOG_LEVEL=debug \
    -it webserver:0.0.1
```

## Environment variables

Environment variables is the main mechanism of manipulating application settings inside a container.

| Variable | Default value | Description |
| --- | --- | --- |
| LISTEN_ADDR | `0.0.0.0` | Specifies the IPv4 address to listen on |
| LISTEN_PORT | `5000` | Specifies the TCP port to listen on|
| LOG_LEVEL | info | Specifies level of logging of event that will be sent to `stdout`. Acceptable values are `info` and `debug` |
