extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	set_process_input(true)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Update cursor position to match mouse position
	global_position = get_viewport().get_mouse_position()
