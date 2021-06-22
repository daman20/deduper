FROM python:3.8
ADD main.py .
ADD deletedupes.py .
ADD makehashes.py .
RUN pip install hashlib json
CMD [ "python", "./main.py" ]
