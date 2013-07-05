#!/bin/bash
echo "Video executing..."

### Old - has no &media=audio
#/opt/python2.7/bin/python2.7 /var/tmp/google_appengine/dev_appserver.py --host 0.0.0.0 /var/tmp/webrtc-samples-read-only/apprtc &

### New - has &media=audio
#/opt/python2.7/bin/python2.7 /var/tmp/google_appengine/dev_appserver.py --host 0.0.0.0 /var/tmp/webrtc-read-only/samples/js/apprtc &

### New
/opt/python2.7/bin/python2.7 /var/tmp/google_appengine/dev_appserver.py --host 0.0.0.0 /var/tmp/google_appengine/webrtc-read-only/samples/js/apprtc &