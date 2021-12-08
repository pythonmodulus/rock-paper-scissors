points = 0
ints = points
def func1():
	import random
	computer1 = ["rock" , "scissor" , "paper"]
	computer = random.choice(computer1)
	human = str(input("enter your choice : "))
	if human == "rock":
		if computer == human:
			print ("draw , computer chose rock")
		elif computer == "paper":	
			print ("computer won , computer chose paper")
			ints = points - 1 
		else:
			print("you won , computer chose scissor")
			ints = points + 1
	if human == "paper":
			if computer == human:
				print("draw , computer chose paper")
			elif computer == "scissor":
				print("you lost , computer chose scissor")
				ints = points - 1
			else:
				print("you won , computer chose rock")
				ints = points + 1
	if human == "scissor":
			if computer == human:
				print("draw , computer chose scissor")
			elif computer == "rock":
				print("you lost , computer chose rock")
				ints = points - 1
			else:
				print("you won , computer chose paper")	
				ints = points + 1								
	print("To restart type 0 or type 1 to exit")
	repeat = int(input("write your preference: "))
	if repeat == 0:
		func1()
	elif repeat == 1:
		print ("your point : " , ints)
		print("exit()")
func1()		