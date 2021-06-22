FROM python:3.8
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
