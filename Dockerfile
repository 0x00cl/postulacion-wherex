FROM docker.io/library/python:3.9-alpine3.20
ARG username=app

RUN apk update && \
    apk upgrade && \
    apk add gcc musl-dev linux-headers

RUN adduser -D $username
ENV PATH=/home/$username/.local/bin:$PATH
RUN echo 'export "PATH=$PATH"' >> /etc/profile

USER $username

RUN pip install gunicorn==22.0.0

WORKDIR /app
COPY --chown=$username:$username . /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "myapp:app"]
