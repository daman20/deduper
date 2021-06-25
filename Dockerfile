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
RUN sudo apt-get install tk
CMD [ "python", "./main.py" ]
