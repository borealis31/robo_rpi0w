# robo_rpi0w

Included: .py code for controlling 4 motor raspberry pi zero with robot 
ir-keytable custom mapping for Elegoo nec remote


pins:
1. asMotor = Motor(27,17)
2. apMotor = Motor(16,16)
3. fsMotor = Motor(16,12)
4. fpMotor = Motor(21,20)
(a/f -> Aft/Forward, s/p -> Starbord/Port)

added to rc.local:
1. ir-keytable -c
2. ir-keytable -w /etc/rc_keymaps/nec_custom.toml
3. /usr/sbin/thd --triggers /etc/triggerhappy/triggers.d/ --deviceglob /dev/input/event*
