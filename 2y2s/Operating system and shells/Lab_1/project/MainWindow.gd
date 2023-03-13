extends Control

var hex_l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

var thread1: Thread
var thread2: Thread
var thread3: Thread

func _ready():
	print(dec2bin(123))
	print(dec2octal(123))
	print(dec2hex(123))
	pass


func dec2bin(n: int) -> String:
	var binary: int = 0
	
	var i = 1
	
	while n > 0:
		binary = binary + ((n%2)*i)
		n = n/2
		i = i * 10
	
	return String(binary)


func dec2octal(n: int) -> String:
	var octal = 0
	var i = 1
	var c
	
	while n != 0:
		c = n % 8
		octal = octal + (c*i)
		n = n / 8
		i = i * 10
	
	return String(octal)


func dec2hex(n: int) -> String:
	if(n <= 0):
		return ''
	var c = n%16
	return dec2hex(n/16)+hex_l[c]


func _calculate(data):
	var n: int = int($MarginContainer/VBoxContainer/HBoxContainer/LineEdit.text)
	
	if data == '2':
		$MarginContainer2/HBoxContainer/VBoxContainer2/LineEdit.text = dec2bin(n)
	elif data == '8':
		$MarginContainer2/HBoxContainer/VBoxContainer8/LineEdit.text = dec2octal(n)
	elif data == '16':
		$MarginContainer2/HBoxContainer/VBoxContainer16/LineEdit.text = dec2hex(n)


func _on_Button_pressed() -> void:
	thread1 = Thread.new()
	thread1.start(self, "_calculate", "2")
	
	thread2 = Thread.new()
	thread2.start(self, "_calculate", "8")

	thread3 = Thread.new()
	thread3.start(self, "_calculate", "16")


func _exit_tree():
	thread1.wait_to_finish()
	thread2.wait_to_finish()
	thread3.wait_to_finish()
