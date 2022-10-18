My son was 7 years old when he had to move to online school. 

Idea: Get him Raspberry Pi with camera, run Google Meet on it, take away keyboard and have a button that switches microphone on and off as teacher wants.

HW:
- Raspberry Pi B 4 (GB RAM)
- camera modul with extra long flex cable to take picture of Beda's workspace
- USB sound card
- Grove LED button
- 2 GPIO jumper cables F-M (cut and solded so they are two females and one male)

SW: Works fine with RaspiOS or Ubuntu Mate. Chrome needs all HW goodies I can give it.
Button simulates pressing ctrl-d, I added two lines into /boot/config.txt

dtoverlay=gpio-key,gpio=17,label="D",keycode=32
dtoverlay=gpio-key,gpio=27,label="Ctrl",keycode=29

Inspiration was taken from this discussion: https://www.raspberrypi.org/forums/viewtopic.php?t=255659

