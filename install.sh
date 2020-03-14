#!/usr/bin/env bash

AA_CONFIG='config/apparmor'

sudo bash -c "
cp config/onion-grater/onionservices.yml /etc/onion-grater.d/
cp bin/onionservices /usr/bin/onionservices
cp $AA_CONFIG/usr.bin.onionservices /etc/apparmor.d/
cp $AA_CONFIG/abstractions/onionservices /etc/apparmor.d/abstractions/
cp $AA_CONFIG/local/usr.bin.onionservices /etc/apparmor.d/local
cp onionservices.py /usr/local/lib/python3.7/dist-packages/
systemctl reload apparmor.service
"
