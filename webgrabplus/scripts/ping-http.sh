#!/bin/sh
# Remplace /bin/ping dans le conteneur WebGrab+Plus.
# Raison : Docker Desktop (Mac) ne relaie pas l'ICMP, donc le contrôle "Checking Internet" de WG++ échoue
# alors que HTTP fonctionne. On simule un ping réussi si un site web répond en HTTPS.
host=""
for a in "$@"; do case "$a" in -*) ;; [0-9]*) [ -z "$host" ] && host="$a" ;; *) host="$a" ;; esac; done
[ -z "$host" ] && host="www.google.com"
if curl -s -o /dev/null --max-time 5 "https://www.google.com" ; then
  echo "PING $host ($host) 56(84) bytes of data."
  echo "64 bytes from $host: icmp_seq=1 ttl=64 time=10.0 ms"
  echo ""
  echo "--- $host ping statistics ---"
  echo "1 packets transmitted, 1 received, 0% packet loss, time 0ms"
  echo "rtt min/avg/max/mdev = 10.0/10.0/10.0/0.000 ms"
  exit 0
fi
echo "--- $host ping statistics ---"
echo "1 packets transmitted, 0 received, 100% packet loss, time 0ms"
exit 1
