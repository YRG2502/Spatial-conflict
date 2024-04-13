extends Button


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _pressed():
	# Assuming the LineEdit node is a sibling of this Button
	var line_edit = get_parent().get_node("LineEdit")
	var username = line_edit.text
	UserSettings.save_username(username)
	get_tree().change_scene_to_file("res://scenes/ConstellationSelection.tscn")
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
