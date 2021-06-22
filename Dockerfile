#Base Image
FROM python:3.8
#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
#Random stuff I found online bc of some errors
RUN apt-get update && apt-get install -y apt-transport-https
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP/ubuntu14/2.x/updates/2.4.2.0 HDP main' >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP-UTILS-1.1.0.20/repos/ubuntu14 HDP-UTILS main'  >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/azurecore/ trusty main' >> /etc/apt/sources.list.d/azure-public-trusty.list
#apt-get management
RUN apt-get update
RUN apt-get install -y build-essential
#install dependencies
RUN pip install -r requirements.txt
#I think this should work
CMD [ "python", "./main.py" ]
