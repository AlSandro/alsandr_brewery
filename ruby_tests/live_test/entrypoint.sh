#!/bin/bash -e

set +e

bundle exec rspec ./smoke_test_live_app.rb

bundle exec rspec ./smoke_test_live_app.rb --only-failures