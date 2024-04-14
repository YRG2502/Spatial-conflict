extends Node2D

var popup_scene = preload("res://scenes/User Interface/RetryPopup.tscn")
var popup_scene = preload("res://scenes/User Interface/LevelClearPopup.tscn")

# Called when the node enters the scene tree for the first time.
func _ready():
	var my_scene = load("res://scenes/User Interface/RetryPopup.tscn")
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_asteroids_area_entered(area):
	print("rocket crash")
	var popup_scene_instance = popup_scene.instantiate()
	add_child(popup_scene_instance)
	pass # Replace with function body.
