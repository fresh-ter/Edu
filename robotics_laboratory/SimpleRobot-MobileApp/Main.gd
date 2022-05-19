extends Control


func _ready():
	pass


func _get_ip():
	return $Label/LineEdit.text


func _on_ForwardButton_pressed():
	var ip = _get_ip()
	
	$HTTPRequest.request(
		"http://"+ip+"/forward"
	)


func _on_StopButton_pressed():
	var ip = _get_ip()
	
	$HTTPRequest.request(
		"http://"+ip+"/stop"
	)


func _on_BackButton_pressed():
	var ip = _get_ip()
	
	$HTTPRequest.request(
		"http://"+ip+"/back"
	)


func _on_RightButton_pressed():
	var ip = _get_ip()
	
	$HTTPRequest.request(
		"http://"+ip+"/right"
	)


func _on_LeftButton_pressed():
	var ip = _get_ip()
	
	$HTTPRequest.request(
		"http://"+ip+"/left"
	)
