FROM alpine:edge
COPY main.py makehashes.py deletedupes.py requirements.txt /
RUN apk update && apk upgrade && apk add python3 py3-pip && python3 -m pip install -r requirements.txt && echo '* 8 * * * python3 main.py --directory /scan' | crontab -
CMD crond -f
