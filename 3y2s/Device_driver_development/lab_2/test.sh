#!/bin/bash
clear
sudo insmod lab2.ko $@
sudo rmmod lab2
sudo dmesg

