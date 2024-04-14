extends Node2D

@onready var label = $Label
@onready var timer = $Timer

# Called when the node enters the scene tree for the first time.
func _start_timer():
	self.visible = true
	self.z_index = 1
	timer.start()

func time_left_to_live():
	var time_left = timer.time_left
	var minute = floor(time_left / 60)
	var second = int(time_left) % 60
	return [minute,second]

func _process(delta):
	var time_left = timer.time_left
	self.get_child(1).modulate = Color(1,0,0,((45-time_left)/45))
	label.text = "%02d:%02d" % time_left_to_live()
	if time_left <= 3 and time_left >= 1:
		self.get_child(1).modulate = Color(0,0,0,0)
		get_tree().change_scene_to_file("res://scenes/MainMenu.tscn")
		self.hide()
		timer.stop()
		

