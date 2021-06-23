#Base Image
FROM python:3.8.10-alpine
#Project Files
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
ADD requirements.txt .
ADD manage.py .
#pip management
RUN pip install --upgrade pip
#install dependencies
RUN pip install -r requirements.txt
#I think this should work
CMD [ "python", "./manage.py" ]
