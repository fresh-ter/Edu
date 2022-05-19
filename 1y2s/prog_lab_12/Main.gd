extends Control

func _ready():
	$HBoxContainer/AnimateButton.disabled = true


func _on_ExitButton_pressed() -> void:
	get_tree().quit()


func _on_FileButton_pressed() -> void:
	$FileDialog.popup_centered_ratio()


func _on_FileDialog_file_selected(path: String) -> void:
	$HBoxContainer/AnimateButton.disabled = false
	
	var filepath = $FileDialog.current_path
	print(filepath)
	
	
	var file = File.new()
	file.open(filepath, file.READ)
	var content = file.get_as_text()
	
	$VBoxContainer/TextEdit.text = content
	
	print (content)
	file.close()


func _on_AboutButton_pressed() -> void:
	$AcceptDialog.popup_centered()
