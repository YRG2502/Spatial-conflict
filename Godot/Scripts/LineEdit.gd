extends LineEdit


# Called when the node enters the scene tree for the first time.
func _ready():
	grab_focus()
	pass # Replace with function body.

func _on_LineEdit_text_entered(new_text):
	get_tree().chage_scene("res://scenes/MainMenu.tscn")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
