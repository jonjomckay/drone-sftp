#!/usr/bin/env python2
import logging
import os
import paramiko, StringIO

from sftpsync import Sftp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

key = os.environ['SFTP_KEY']

os.mkdir('/root/.ssh')

with open("/root/.ssh/id_rsa", 'w') as key_file:
    os.chmod("/root/.ssh/id_rsa", 0600)
    key_file.write(key.replace('\\n', '\n'))

sftp = Sftp(os.environ['PLUGIN_HOST'], os.environ['PLUGIN_USER'], port=os.getenv('PLUGIN_PORT', 22), key_filename='/root/.ssh/id_rsa')

excludes = os.getenv('PLUGIN_EXCLUDE', '')

exclude = []

if excludes:
	for e in excludes.split(','):
		exclude.append(e)

sftp.sync(os.environ['PLUGIN_SOURCE'], os.environ['PLUGIN_TARGET'], download=False, exclude=exclude, delete=True)