extends GridContainer

var containerSize = columns**2
var random_number = randi() % 9
var meth_mined = 0
var meth_required = 1
# Called when the node enters the scene tree for the first time.
func _ready():
	var button = get_child(random_number)	
	button.text = "White Ore"
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
