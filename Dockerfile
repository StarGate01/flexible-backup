FROM alpine:3.11

RUN apk add --no-cache docker-cli ca-certificates bash tzdata python3 py3-pip

COPY pybku /app/pybku
#RUN pip3 install requests

WORKDIR /app/pybku
ENTRYPOINT [ "python3", "/app/pybku/pybku.py" ]