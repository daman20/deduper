#Base Image
FROM python:3.8.10-alpine
#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
ADD requirements.txt .
ADD guifunctions.py .
#pip management
RUN pip install --upgrade pip
#install dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install tk-dev && rm -r /var/lib/apt/lists/*
RUN export uid=99 gid=100 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer
USER developer
ENV HOME /home/developer
CMD [ "python", "./main.py" ]
