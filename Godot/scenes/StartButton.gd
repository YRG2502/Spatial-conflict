extends Button


# Called when the node enters the scene tree for the first time.
func _ready():
	var button = Button.new()
	button.text = "press me"
	button.pressed.connect(self._button_pressed)
	pass # Replace with function body.

func _button_pressed():
	print("Hello world")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
