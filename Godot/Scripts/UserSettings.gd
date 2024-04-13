# UserSettings.gd
extends Node

var username := ""

func save_username(new_username: String):
	username = new_username
	# You could also save to disk here using File

func get_username() -> String:
	return username

