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
##Add tkinter
RUN apk add python3-tkinter
# Install vnc, xvfb in order to create a 'fake' display
RUN     apk add x11vnc xvfb
RUN     mkdir ~/.vnc
# Setup a password
RUN     x11vnc -storepasswd 1234 ~/.vnc/passwd
ENV DISPLAY localhost:5900
EXPOSE 5900
CMD [ "python", "./main.py" ]
