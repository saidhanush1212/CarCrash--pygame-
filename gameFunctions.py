import pygame
from pygame.locals import *
import random

pygame.init()

#setting up screen parameters
width = 700
height = 600

#setting up street lights
light = pygame.image.load('light.png')

#setting up colours 
#            R    G    B 
GRAY     = (100, 100, 100) 
NAVYBLUE = ( 60,  60, 100) 
WHITE    = (255, 255, 255) 
RED      = (255,   0,   0) 
GREEN    = (  0, 255,   0) 
BLUE     = (  0,   0, 255) 
YELLOW   = (255, 255,   0) 
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255) 
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
LIGHTGREEN = (50, 205, 50)
LIGHTGREY = (169, 169, 169)

#car width and height
carWidth = 40
carHeight = 59

#car class definition
class carOpp:
	carWidth = 40
	carHeight = 74

	def __init__(self,imagePath):
		self.isCarOpp = False #to check if a car is coming opposite
		self.carOppY = -1
		self.carOppX = 0
		self.carOpp = pygame.image.load(imagePath)

'''def startGamePage():
	
	use - to draw a screen which will show the start of the game!!
	parameters - None
	return value - None
	
	# function definition
'''
	
def isInContact(CarX,CarY,obstacleX,obstacleY):
	'''
	use - to check if the car crashes with another car or an object(such as a pothole), so that the car's health can be 
	reduced appropriately
	parameters - CarX,CarY : the x and y co-ordinates of the car
				 Obstacle_width,obstacle_height : the width and height of the obstacle
	return value - Boolean(True/False)
	'''
	carWidth = 40
	carHeight = 59
	obstacle_width = 45
	obstacle_height = 80

	if (CarY < obstacleY+obstacle_height and CarY > obstacleY) or ( CarY + carHeight >obstacleY and CarY + carHeight < obstacleY + obstacle_height):
		if ((CarX > obstacleX and CarX < obstacleX + obstacle_width) or (CarX+carWidth > obstacleX and CarX + carWidth < obstacleX+obstacle_width)):
			#returns true if there is a contact
			return True 
	return False

def genObstacleX(roadStartX,roadEndX):
	'''
	use - to randomly generate the x co-ordinate of the obstacle coming opposite by using random function. 
	Note - the x co-ordinate must lie within the x-coordinates of the road
	parameters -roadStartX,roadEndX: to find out where the road starts and ends
	returns - the x-coordinate
	'''
	x = random.randrange(roadStartX,roadEndX)
	return x

def checkBoundaryPos(carX, carY, roadStartX, roadEndX):
	'''
	use - to check if the car is going off the road.
	parameters - carX, carY :the x and y coordinates of the car
				roadStartX, roadEndX : the start and end positions of teh road
				leftSideWalk, rightSideWalk : the x coordinates of the side walks.
	return - position of car as string
	'''
	if (carX>roadStartX and carX<roadEndX):
		return True
	return False


def reduceHealth(health, obstacle):
	'''
	use - to reduce the health depending on what obstacle the car is getting hit by
	parameters - health of the car, the obstacle as a string('pothole'/'car'/''.....if it is an empty string, 
				health remains same)
	return  - the new health
	'''
	if obstacle == 'pothole':
		health = health-10
		return health

	elif obstacle == 'car':
		health = health-50
		return health

	elif obstacle == '':	
		return health

def message_display(gameDisplay,text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf = largeText.render(text, True, BLACK)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	

def crash(gameDisplay):
	message_display(gameDisplay,'You Crashed')
	pygame.time.delay(50)

def appendCarList(carList):
	'''
	use - to add a car to the opposite side as time passes
	parameters - carList : the list of cars which are already there
	return - the new list with the car added
	'''
	carType = random.choice(['blueCar.png','yellowCar.png','blackCar.png','ambulance.png','orangeCar.png','truck.png'])
	carList.append(carOpp(carType))


	