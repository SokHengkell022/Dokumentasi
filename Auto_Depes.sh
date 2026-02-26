#!/usr/bin/Bash

BLC='\033[1;30m'
BG='\033[41m'
PUT='\033[97m'
N='\033[0m'
R='\033[0;31m'
G='\033[0;32m'
O='\033[0;33m'
P="\033[2m"
BL='\033[0;96m'
B='\033[1;36m'
BR="\033[0;34m"
U="\033[0;35m"
time_out="30"

trap 'echo "gaboleh keluar loh ya";' SIGINT SIGTSTP SIGTERM

while True; do
    echo -e "gabisa CTRL wok"
    sleep 2
done

clear
echo -e "                        \033[7;36mHallo Broo${N}
                                 /
         ░░░░░░░▄█▄▄▄█▄  /          ${N}\033[3;35By Tools Ubah Tema juned${N}
         ▄▀░░░░▄▌─▄─▄─▐▄ ░░░▀▄   ${R}Agressiv${N}
         █▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█   ${O}./Juned${O}3${O}n${N} 
         ░▐▌░░░░▀▀███▀▀░░░░▐▌
         ████░▄█████████▄░████
         "
         
echo -e "${BG}${BLC}BENTAR CEK MODULE DULU WOK${N}"
sleep 2

clear
#====Install Module====
pip install sys
pip install requests
pip install telebot
pip install subprocess

clear
sleep 1
python3 mainnn.py
