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
#RUN \
#    APP_ICON_URL=https://raw.githubusercontent.com/daman20/deduper/master/Deduper%20Logo.png && \
#    APP_ICON_DESC='{"masterPicture":"/opt/novnc/images/icons/master_icon.png","iconsPath":"/images/icons/","design":{"ios":{"pictureAspect":"noChange","assets":{"ios6AndPriorIcons":false,"ios7AndLaterIcons":false,"precomposedIcons":false,"declareOnlyDefaultIcon":true}},"desktopBrowser":{"design":"raw"},"windows":{"pictureAspect":"noChange","backgroundColor":"#da532c","onConflict":"override","assets":{"windows80Ie10Tile":false,"windows10Ie11EdgeTiles":{"small":false,"medium":true,"big":false,"rectangle":false}}},"androidChrome":{"pictureAspect":"noChange","themeColor":"#ffffff","manifest":{"display":"standalone","orientation":"notSet","onConflict":"override","declared":true},"assets":{"legacyIcon":false,"lowResolutionIcons":false}},"safariPinnedTab":{"pictureAspect":"silhouette","themeColor":"#5bbad5"}},"settings":{"scalingAlgorithm":"Mitchell","errorOnImageTooSmall":false,"readmeFile":false,"htmlCodeFile":false,"usePathAsIs":false}}' && \
#    install_app_icon.sh "$APP_ICON_URL" "$APP_ICON_DESC"
ENV KEEP_APP_RUNNING=1
ENV APP_NAME="Deduper"
USER_ID=99
GROUP_ID=100
RUN echo "python3 /main.py" > ~/.xinitrc && chmod +x ~/.xinitrc
