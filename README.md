# robo_rpi0w
.py code for controlling 4 motor raspberry pi zero w robot

added to rc.local:
1. ir-keytable -c
2. ir-keytable -w /etc/rc_keymaps/nec_custom.toml
3. /usr/sbin/thd --triggers /etc/triggerhappy/triggers.d/ --deviceglob /dev/input/event*
