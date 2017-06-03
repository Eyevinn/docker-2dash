# Docker to DASH

This is a Docker container to pre-package MPEG DASH on demand content. It is based on Bento4.

## Install

Make sure you have Docker installed and can run Docker containers on your computer. Then download and
install the helper script

```
# curl -L https://github.com/eyevinn/docker-2dash/releases/download/mp4todash > /usr/local/bin/mp4todash
```

This is a helper script that runs the container with a pre-defined set of arguments to start the container

## Create MPEG DASH from MP4s

Place yourself in the directory where you have the MP4s (one MP4 per bitrate) and then run:

```
$ mp4todash example-1920-4500.mp4 example-720-1500.mp4
```