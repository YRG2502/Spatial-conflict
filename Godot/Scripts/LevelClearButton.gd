extends Button

@export var redirect_scene = "res://scenes/ConstellationSelection.tscn"

# Called when the node enters the scene tree for the first time.
func _ready():

	get_tree().paused = true
	pass # Replace with function body.

func _pressed():
	get_tree().paused = true
	get_tree().change_scene_to_file(redirect_scene)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
