#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/fusion/")
sys.path.insert(0,"/var/www/fusion/fusion/")

import logging
logging.basicConfig(stream=sys.stderr)

from fusion import app as application