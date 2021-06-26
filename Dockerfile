# Pull base image.
FROM jlesage/baseimage-gui:alpine-3.6

# Install xterm.
RUN add-pkg xterm

# Copy the start script.
COPY startapp.sh /startapp.sh

# Set the name of the application.
ENV APP_NAME="Deduper"
#Project Files
ADD main.py /
ADD deletedupes.py /
ADD makehashes.py /
ADD requirements.txt .
ADD guifunctions.py /
#install python
RUN add-pkg python3
RUN add-pkg py3-pip
#pip management
RUN pip3 install --upgrade pip
#install dependencies
RUN pip3 install -r requirements.txt
##Add tkinter
RUN add-pkg python3-tkinter
## Set ENVS
# Generate and install favicons.
RUN \
    APP_ICON_URL=https://github.com/daman20/deduper/blob/27cc9ef55776361e3a3f507cd4985cec5c8c8cfc/Deduper%20Logo.png && \
    install_app_icon.sh "$APP_ICON_URL"
ENV KEEP_APP_RUNNING=1
RUN echo "python3 /main.py" > ~/.xinitrc && chmod +x ~/.xinitrc
