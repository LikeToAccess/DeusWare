from noise import pnoise2
from time import sleep
from threading import Thread
import os
import color
import platform
import socket

try: from pynput import keyboard
except ImportError: keyboard = None

# unused ports: 26490-26999
port = 26969
address = "192.168.50.172"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
width, height = 80, 40
octaves = 1
frequency = 200 * octaves
sea_level = 15
coordinates = []
local_coordinates = (200,50)
x_change = 0
y_change = 0
direction = None
speed = 1
system = platform.system()
delay = 0.065 if "Windows" in system else 0.65

if keyboard:
	keyboard_controller = keyboard.Controller()


def connect(address=socket.gethostbyname(socket.gethostname()), port=26490):
	print("Connecting to \"{0}:{1}\"...".format(address,port))
	s.connect((address, port))
	print("Connected!")

def recv(buffer=1024, encoding="utf8"):
	msg = s.recv(buffer).decode(encoding)
	return msg

def send(msg, encoding="utf8"):
	if msg.strip() != "":
		s.send(msg.encode(encoding))

def compress_list(data):
	compressed = f"{data[0]},{data[1]}"
	return compressed

def recv_coordinates():
	pairs = recv().split("|")  # ['215,55', '235,52']
	msg = []
	for pair in pairs:
		pair = pair.split(",")  # ['215', '55']
		coordinate_pair = []
		for coordinate in pair:
			coordinate_pair.append(int(coordinate))
		msg.append(tuple(coordinate_pair))
	print(msg)
	sleep(0.5)
	return msg

def on_release(key):
	global direction
	if key:
		direction = key

def start():
	keyboard_listener = keyboard.Listener(on_release=on_release)
	keyboard_listener.start()

if keyboard:
	threaded_function = Thread(target=start)
	threaded_function.start()

connect(address=address, port=port)
for i in range(1000):
	frame_buffer = []
	coordinates = recv_coordinates()
	print(f"Recieved {coordinates}")
	x_change, y_change = local_coordinates
	packet = compress_list(local_coordinates)
	send(packet)
	if direction:
		direction = str(direction)
		if "w" in direction:
			y_change -= speed
		elif "a" in direction:
			x_change -= speed
		elif "s" in direction:
			y_change += speed
		elif "d" in direction:
			x_change += speed
		direction = None

	for y in range(height):
		frame_buffer.append("|")
		for x in range(width):
			n = int(pnoise2(x/(frequency+2)+x_change/frequency, y/(frequency+1)+y_change/frequency, int(octaves))*sea_level)
			n = str(n) if n >= 1 else " "
			n = "9" if len(n) > 1 else n
			n = color.highlight(" ", n)

			for count, player in enumerate(coordinates):
				if y+y_change == coordinates[count][1] and x+x_change == coordinates[count][0]:
					n = "\033[1;31m!\033[1;m"
			
			if y == int(height/2) and x == int(width/2):
				frame_buffer.append("\033[1;31m!\033[1;m")
				local_coordinates = (x_change, y_change)
			else:
				frame_buffer.append(n)
		frame_buffer.append("|\n")
	os.system("cls" if "Windows" in system else "clear")
	print("".join(frame_buffer))
	print(f"{coordinates}+{local_coordinates}")
	
	#sleep(delay)

