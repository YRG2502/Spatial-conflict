# UserSettings.gd
extends Node

var username := ""
var ans

func save_username(new_username: String):
	username = new_username
	# You could also save to disk here using File

func get_username() -> String:
	return username

func save_ans(new_answer: int):
	ans = new_answer
	
func get_ans() -> int:
	return ans
