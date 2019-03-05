#!/usr/bin/env python3

from urllib.parse import urlsplit
import sys
import re

try:
    url = sys.argv[1]
except IndexError:
    print('Too few arguments. Use punycode <hostname>')
    quit(1)

# If url without schema, for correct urlsplit work, add http://

if not re.match(r'http(s?)\:', url):
    url = 'http://' + url

# Split url to scheme, netloc, path

parsed = urlsplit(url)

host = parsed.netloc

# Remove 'www.' for old-schoolers

if host.startswith('www.'):
    host = host[4:]

# Encode/Decode inputstring
try:
    print(host.encode('utf8').decode('idna'))
except UnicodeDecodeError as ex:
    print(host.encode('idna').decode('utf8'))