extends Node2D

var pickaxe

# Called when the node enters the scene tree for the first time.
func _ready():
	# Load the pickaxe scene
	pickaxe = preload("res://scenes/Planets/Pickaxe.tscn").instantiate()
	add_child(pickaxe)

func _input(event):
	# Track mouse movement
	if event is InputEventMouseMotion:
		# Update cursor position
		pickaxe.global_position = event.position

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
