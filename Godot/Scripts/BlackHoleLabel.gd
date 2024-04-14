extends Label


# Called when the node enters the scene tree for the first time.
func _ready():
	var username = UserSettings.get_username()
	self.text = "Captain " + username + ", quickly activate the time machine
 before you get sucked into the black hole"
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
