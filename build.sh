#!/bin/bash

bundle exec jekyll build
rsync -v -rz --checksum _site/ adulau@kb.quuxlabs.com:/home/adulau/website/misp.software
