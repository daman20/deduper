#Base Image
FROM python:3.8.10-alpine
#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
ADD requirements.txt .
#pip management
RUN pip install --upgrade pip
#install dependencies
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
