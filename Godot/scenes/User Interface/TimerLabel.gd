extends Node2D

@onready var label = $Label
@onready var timer = $Timer

# Called when the node enters the scene tree for the first time.
func _ready():
	self.z_index = 1
	pass # Replace with function body.

func _start_timer():
	
	timer.start()

func time_left_to_live():
	var time_left = timer.time_left
	var minute = floor(time_left / 60)
	var second = int(time_left) % 60
	return [minute,second]

func _process(delta):
	label.text = "%02d:%02d" % time_left_to_live()

