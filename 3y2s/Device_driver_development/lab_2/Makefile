obj-m += lab2.o

all:
	make -C /lib/modules/$(shell uname -r)/build M='$$(PWD)' modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M='$$(PWD)' clean
test:
	sudo dmesg -C
	sudo insmod lab2.ko
	sudo rmmod lab2.ko
	sudo dmesg
