#!/bin/sh

set -e

envsubst < /ect/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'