#!/bin/bash -e

set +e

cd pytest

pytest -s --url https://my.daqri.com

pytest -s --url https://my.development.daqri.info