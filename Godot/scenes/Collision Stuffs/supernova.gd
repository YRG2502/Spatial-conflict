extends Area2D

@export var rotation_speed = 1
@export var size = 0.6

# Called when the node enters the scene tree for the first time.

func _ready():
	self.scale.x = size
	self.scale.y = size
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	self.rotation += rotation_speed * 0.5
	self.scale.x += 0.005
	self.scale.y +=0.005
	pass
