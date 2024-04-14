extends Button


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _pressed():
	var text = get_node("../TextEdit")
	print("lol")
	text.hide()
	self.hide()
	get_tree().paused = false

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
