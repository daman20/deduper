FROM alpine:edge
COPY main.py makehashes.py deletedupes.py requirements.txt /
RUN apk add python3 py3-pip && python3 -m pip install -r requirements.txt
