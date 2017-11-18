FROM python:3.6-alpine
RUN apk add --update --no-cache gcc g++ postgresql-dev && \
    apk add --no-cache tini && apk add --no-cache libffi-dev
WORKDIR /app
COPY ["requirements.txt", "/app"]
COPY ["setup.py", "/app"]
RUN pip install -qr requirements.txt
COPY . .

# Set the application environment
ENV PYTHONIOENCODING utf_8
ENV PYTHONPATH /app:$PYTHONPATH
ENV PATH="/app/bin:${PATH}"

# Run as User
#RUN adduser -D myuser
#USER myuser

RUN chmod +x bin/docker-entrypoint.sh

CMD ["bin/docker-entrypoint.sh", "wsgi:app"]
