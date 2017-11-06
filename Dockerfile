FROM python:3.6-alpine
RUN apk add --update --no-cache gcc g++ postgresql-dev && \
    apk add --no-cache tini
WORKDIR /app
COPY ["requirements.txt", "/app"]
RUN pip3 install -qr requirements.txt
COPY . .

# Set the application environment
ENV PYTHONIOENCODING utf_8
ENV PYTHONPATH /app:$PYTHONPATH
ENV PATH="/app/bin:${PATH}"

# Heroku recommends running as a user but it didn't work
# FIXME: fix running docker container as user in dockerfile on Heroku
# Run as User
#RUN adduser -D myuser
#USER myuser

RUN chmod +x bin/entrypoint.sh

# The entry point with tini is not working on heroku
# ENTRYPOINT ["/usr/sbin"]
# FIXME: fix entrypoint for tini not working in dockerfile on Heroku
CMD ["/tini", "--", "bin/docker-entrypoint.sh", "wsgi:app"]
