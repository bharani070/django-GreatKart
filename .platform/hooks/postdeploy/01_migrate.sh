#!/bin/bash

source /var/app/venv/*/bin/activate && { python migrate.py createsuperuser --noinput; }

