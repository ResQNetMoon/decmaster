mkdir /opt/decmaster
cp decoder.py /opt/decmaster
cp getarg.py /opt/decmaster

echo 'cd /opt/decmaster && python3 /opt/decmaster/decoder.py "$@"' > /usr/bin/decmaster

chmod 777 /usr/bin/decmaster
