extends Button


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _pressed():
	var line_edit = get_parent().get_node("LineEdit")
	var user_ans = line_edit.text
	var real_ans = str(UserSettings.get_ans())
	if user_ans == real_ans:
		print("True")
		get_tree().change_scene_to_file("res://scenes/SolarSystem.tscn")
	else:
		line_edit.text = ""
		print("False")
		

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
