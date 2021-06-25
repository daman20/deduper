# Pull base image.
FROM ubuntu:latest
RUN apt-get update && apt-get install -y x11vnc xvfb
RUN echo "exec firefox" > ~/.xinitrc && chmod +x ~/.xinitrc
CMD ["v11vnc", "-create", "-forever"]

#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
ADD requirements.txt .
ADD guifunctions.py .
#install python
RUN apt-get python3
#pip management
RUN pip install --upgrade pip
#install dependencies
RUN pip install -r requirements.txt
##Add tkinter
RUN apt-get python3-tkinter
ENV DISPLAY=127.0.0.1:0.5900
RUN echo "python3 main.py" > ~/.xinitrc && chmod +x ~/.xinitrc