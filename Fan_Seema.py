speed = 0
while 1:
  corddir = int(input('Press 1 to increase the speed.\nPress 2 to reverse the direction\n'))
  if corddir == 1:
    if speed == 3:
      speed == 0
      print("Fan is Off ")
    else:
      speed+=1
      print("Speed is :", speed)
  elif corddir == 2:
    speed = (-1) * speed
    print("Direction is reversed and the speed is :", speed)
  else:
    raise Exception("Invalid Cord Direction")
