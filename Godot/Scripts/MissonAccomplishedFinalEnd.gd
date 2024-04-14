extends Node2D
var clear_scene = preload("res://scenes/StarSystemSelection.tscn")

# Called when the node enters the scene tree for the first time.
func _ready():
	TimerLabel.hide()
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_clear_area_area_entered(area):
	print("CLEARRRR")
	var clear_scene_instance = clear_scene.instantiate()
	add_child(clear_scene_instance)
	pass # Replace with function body.
