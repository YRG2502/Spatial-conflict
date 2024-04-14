extends Label

var num1 = randi() % 100 + 1
var num2 = randi() % 100 + 1
var mult_ans = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	self.text = str(num1) + " x " + str(num2)
	mult_ans = num1 * num2
	UserSettings.save_ans(mult_ans)
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
