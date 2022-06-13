#!/bin/bash

PATH="/usr/local/bin:/usr/local/sbin:$PATH"

cd /home/nalepova/aka-service/service

ps aux | grep -f pid || ./run.sh start
