#Base Image
FROM python:3.8
#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
#Random stuff I found online bc of some errors
RUN apt-get update && apt-get install -y apt-transport-https
#apt-get management
RUN apt-get update
RUN apt-get install -y build-essential
#install dependencies
RUN pip install -r requirements.txt
#I think this should work
CMD [ "python", "./main.py" ]
