#!/bin/bash

# Limitation
# 1) SIGKILL cannot be caught, if the program is kill by SIGKILL(9), you need to manually remove the lock dir.

LOCK_DIR=/tmp/myapp.lock

# If there is another same script running, quit.
if ! mkdir "${LOCK_DIR}" >/dev/null 2>&1; then
echo "Another $(basename "$0") is already running!"
    exit
fi

# Remove lock dir on exit
trap "rm -rf ${LOCK_DIR} && exit 255" EXIT SIGHUP SIGTERM SIGQUIT

# Do your tasks...
while :
do
    echo "doing jobs"
    sleep 1
done
