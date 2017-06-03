FROM eyevinntechnology/packager-base:0.1.0
MAINTAINER Eyevinn Technology <info@eyevinn.se>
RUN apt-get update && apt-get install -y --force-yes curl
RUN pip install hlsdownload==0.0.13
COPY entrypoint.py /root/entrypoint.py
ENTRYPOINT ["/root/entrypoint.py"]
CMD []
