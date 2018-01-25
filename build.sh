#!/bin/bash

bundle exec jekyll build
cp -rf .well-known/ _site/
rsync --include ".*" -v -rz --checksum _site/ adulau@kb.quuxlabs.com:/home/adulau/website/misp.software
