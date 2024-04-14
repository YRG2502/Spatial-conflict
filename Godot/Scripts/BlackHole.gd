extends Sprite2D

# Gravitational constant
var GRAVITY = 5  # Adjust this value as needed

# The sprite representing the rocket
var rocket: Node2D

# Called when the node enters the scene tree for the first time.
func _ready():
	# Find the rocket node in the scene
	rocket = get_node("/root/BlackHole/Rocket")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Calculate the direction vector from this sprite to the rocket
	var direction = rocket.global_position - global_position
	direction = direction.normalized()
	
	# Calculate the gravitational force
	var force = direction * GRAVITY
	
	# Apply the force to the rocket
	rocket.global_position -= force * delta
	
	# Increase the gravity as you get closer
	GRAVITY += 0.1
