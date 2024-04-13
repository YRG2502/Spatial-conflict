extends LineEdit


# Called when the node enters the scene tree for the first time.
func _ready():
	grab_focus()
	pass # Replace with function body.

func _on_LineEdit_text_entered(new_text):
	UserSettings.save_username(new_text)
	return new_text

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
