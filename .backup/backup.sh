#!/bin/bash

backupdir="$HOME/.backup"
archlinuxdir="$HOME/.backup/archlinux"
datedir="$archlinuxdir/$(date "+%Y_%m_%d_%H_%M_%S")"

if [ ! -e $backupdir ]; then
    mkdir $backupdir
fi

if [ ! -e $archlinuxdir ]; then
    mkdir $archlinuxdir
fi

mkdir $datedir
cd $datedir
pacman -Qq > "archlinux_packages.list"
cp /etc/pacman.conf pacman.conf
cp /etc/default/grub grub
