FROM ruby:2.6.3-stretch

# Install essential Linux packages
# RUN apt-get update -qq && apt-get install -y \
#    build-essential


RUN mkdir -p /srv/test
WORKDIR /srv/test

COPY . .

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

RUN mkdir -p /srv/test/data

# COPY ./spec/support/data/avatar.png /srv/test/data/avatar.png

# Install dependencies
RUN gem update --system
RUN gem install bundler && bundle install

# ENTRYPOINT [ "/srv/test/entrypoint.sh" ]
