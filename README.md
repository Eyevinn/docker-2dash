# Docker to DASH

This is a Docker container to pre-package MPEG DASH on demand content. It is based on Bento4.

## Install

Make sure you have Docker installed and can run Docker containers on your computer. Then download and
install the helper script

```
curl -L https://github.com/Eyevinn/docker-2dash/releases/download/v0.0.3/mp4todash > /usr/local/bin/mp4todash
chmod +x /usr/local/bin/mp4todash
curl -L https://github.com/Eyevinn/docker-2dash/releases/download/v0.0.3/hlstodash > /usr/local/bin/hlstodash
chmod +x /usr/local/bin/hlstodash
```

This is a helper script that runs the container with a pre-defined set of arguments to start the container

## Create MPEG DASH from MP4s

Place yourself in the directory where you have the MP4s (one MP4 per bitrate) and then run:

```
$ mp4todash example-1920-4500.mp4 example-720-1500.mp4
```

## Create MPEG DASH from HLS VOD

```
$ hlstodash http://example.com/file/master.m3u8
```
