#!/bin/bash
# Will be executed as user "root".
TMPFILE=$LBPDATA/$3/newrootpassword
PASSWORD=`tr -dc A-Za-z0-9 </dev/urandom | head -c 13 ; echo ''`
echo $PASSWORD > $TMPFILE
chmod 0600 $TMPFILE
chown loxberry:loxberry $TMPFILE
echo root:$PASSWORD | chpasswd
exit 0
