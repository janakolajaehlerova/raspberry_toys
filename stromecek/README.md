3D RGB x-mas tree + Raspberry Zero

Purpose: x-mas lights for university lecture 

Installation: 
2021-10-30-raspios-bullseye-armhf-lite.img
add wifi
apt-get install vim git python3-tk
change user pi my_user
usermod -l my_user pi
cat /etc/shadow
passwd my_user
cat /etc/passwd
mv /home/pi/ /home/my_user
vim /etc/group #check for pi user in all files like:
vim /etc/sudoers
vim /etc/subuid 
vim /etc/subgid 
vim /etc/systemd/system/autologin@.service 

Get the code for xmastree:
git clone https://github.com/rendzina/XmasTree.git
wget https://bit.ly/2Lr9CT3 -O tree.py

Make it work automatically so I don't have to do anything in front of the students:
Add into crontab:
@reboot path_to_my_script

Turn off the lights in auditorium :)
