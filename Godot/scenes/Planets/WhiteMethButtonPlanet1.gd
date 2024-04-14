extends Button

var grid_container 
# Called when the node enters the scene tree for the first time.
func _ready():
	grid_container = get_parent()
	pass # Replace with function body.

func _pressed():
	if get_text() == "White Ore":
		print("Successful")
		grid_container.meth_mined += 1
		if grid_container.meth_mined == grid_container.meth_required:
			get_tree().change_scene_to_file("res://scenes/Planets/Planet2.tscn")
			
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
