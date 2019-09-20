#!/usr/bin/python
import sys
import logging
import os


logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/app_folder/config/')
sys.path.append('/var/www/app_folder/pages/')
sys.path.append('/var/www/app_folder/')



os.chdir("/var/www/app_folder")


from app_main import app as application

#application.run(host="0.0.0.0", port=5000)
