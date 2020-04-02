FROM alpine:3.11

RUN apk add --no-cache bash

COPY scripts /app/scripts

WORKDIR /app/scripts
CMD [ "./service.sh" ]