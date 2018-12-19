FROM python:3

WORKDIR /usr/src/app
RUN pip install flask

ADD . .


EXPOSE 5000 80

CMD [ "python", "./flaskapp.py" ]