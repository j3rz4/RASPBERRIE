'''
sync omxplayer on Raspberry Pi over dbus with Python

references:
https://github.com/andresromero/RPI-Cast/blob/master/omxplayer-dbus.py
https://github.com/popcornmix/omxplayer/blob/master/README.md#dbus-control
'''
import dbus
import time
import datetime

count = 0
time.sleep(10)
while count<5:
    count+=1
    try:
        with open('/tmp/omxplayerdbus.root', 'r+') as fd:
            sock_info = fd.read().strip()
            bus = dbus.bus.BusConnection(sock_info)

            obj = bus.get_object('org.mpris.MediaPlayer2.omxplayer1',
                '/org/mpris/MediaPlayer2', introspect=False)
            omxpro = dbus.Interface(obj, 'org.freedesktop.DBus.Properties')
            omxpla = dbus.Interface(obj, 'org.mpris.MediaPlayer2.Player')
            p = omxpro.Position()
            break
    except:
        print('error')

#print (ifp.Duration()) # in microseconds, one second is 1,000,000
p=0
t2=0
t = datetime.datetime.now()
t2=(t.second*1000000)+t.microsecond-10000000
omxpla.SetPosition(dbus.ObjectPath('/not/used'),dbus.Int64(t2))
p = omxpro.Position()
print ('pos',p, t ,t2)

