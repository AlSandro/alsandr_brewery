FROM python:3.7


RUN mkdir -p /srv/test

WORKDIR /srv/test

COPY . .

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

RUN mkdir -p /srv/test/data


# install selenium
RUN pip install selenium

RUN pip install -r ./pytest/requirments.txt