FROM python:3.9.9

#RUN apk add --update ca-certificates;

EXPOSE 5000
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ../ /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /var/cache/apk/*

CMD gunicorn -w 7 -b 0.0.0.0:5000 wsgi:app
