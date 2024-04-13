extends CharacterBody2D

@export var speed = 4
@export var acceleration = 800

var target = position
var enable_movement = false



func _input(event):
	if event.is_action_pressed("ui_mouse_left") and enable_movement == false:
		enable_movement = true
		get_node("Label").queue_free()
	pass

func _physics_process(delta):
	if enable_movement:
		target = get_global_mouse_position()
		velocity = position.direction_to(target) * speed * position.distance_to(target)
		look_at(target)
	else:
		velocity
	if position.distance_to(target) > 10:
		move_and_slide()

func _on_area_2d_body_entered(body):
	print("entered", body)
	pass # Replace with function body.


func _on_area_2d_body_exited(body):
	print("exited", body)
	pass # Replace with function body.
