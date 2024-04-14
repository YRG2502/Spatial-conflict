extends Button

var grid_container 
var textbox
var hideBtn
# Called when the node enters the scene tree for the first time.
func _ready():
	grid_container = get_parent()
	var colorRect = grid_container.get_parent()
	var scene = colorRect.get_parent()
	textbox = scene.get_node("ColorRect/TextEdit")
	hideBtn = scene.get_node("ColorRect/HideTextBtn2")
	pass # Replace with function body.

func _pressed():
	z_index += 50
	var theme = Theme.new()
	if get_text() == "White Ore":
		theme.set_color("button_normal", "Button", Color(0, 0, 1))
		set_theme(theme)
		grid_container.meth_mined += 1
		if grid_container.meth_mined == grid_container.meth_required:
			textbox.visible = true
			hideBtn.visible = true
			grid_container.set_process_input(false)
			#get_tree().change_scene_to_file("res://scenes/Planets/Planet2.tscn")
	else:
		theme.set_color("button_normal", "Button", Color(1, 0, 0))
		set_theme(theme)
			
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
