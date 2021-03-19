def color(msg, color):
	color = color.lower()
	if color == "black":
		return f"\033[1;30m{msg}\033[1;m"
	elif color == "red":
		return f"\033[1;31m{msg}\033[1;m"
	elif color == "green":
		return f"\033[1;32m{msg}\033[1;m"
	elif color == "yellow":
		return f"\033[1;33m{msg}\033[1;m"
	elif color == "blue":
		return f"\033[1;34m{msg}\033[1;m"
	elif color == "magenta":
		return f"\033[1;35m{msg}\033[1;m"
	elif color == "cyan":
		return f"\033[1;36m{msg}\033[1;m"
	elif color == "gray":
		return f"\033[1;37m{msg}\033[1;m"
	else:
		return str(msg)
	
def highlight(msg, color):
	color = color.lower()
	# black
	if color == "black":
		return f"\033[1;40m{msg}\033[1;m"
	# red
	elif color == "red":
		return f"\033[1;41m{msg}\033[1;m"
	# green / grass
	elif color == "3" or color == "4" or color == "5":
		return f"\033[1;42m{msg}\033[1;m"
	elif color == "6" or color == "7":
		return "\033[1;42m▓\033[1;m"  # ▓▒░
	# orange / sand
	elif color == "2":
		return f"\033[1;43m{msg}\033[1;m"
	# blue / deep water
	elif color == " ":
		return f"\033[1;44m{msg}\033[1;m"
	# magenta
	elif color == "magenta":
		return f"\033[1;45m{msg}\033[1;m"
	# cyan / water
	elif color == "1":
		return f"\033[1;46m{msg}\033[1;m"
	# gray / mountain
	elif color == "8" or color == "9":
		return f"\033[1;47m{msg}\033[1;m"
	else:
		return str(msg)
	
		
