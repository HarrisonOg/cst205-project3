import random, pygame, sys
from pygame.locals import*

FPS = 30
GAMEWIDTH = 800
GAMEHEIGHT = 600
TILESIZE = 40
TILEWIDTH = int(GAMEWIDTH / TILESIZE)
TILEHEIGHT = int(GAMEHEIGHT / TILESIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)
PURPLE = (160, 32, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUNDCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
	global FPSCLOCK, GAMEWINDOW, BASICFONT, time

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	GAMEWINDOW = pygame.display.set_mode((GAMEWIDTH,GAMEHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
	pygame.display.set_caption('test')
	while True:
		runGame()
			
def runGame():

	startx = random.randint(0,TILEWIDTH - 1)
	starty = random.randint(0,TILEHEIGHT - 1)
	playerLocation = {'x': startx, 'y': starty}
	negativeLocation = {'x': -1, 'y': -1}
	negativeSpawn = 0
	reverseLocation = {'x': -1, 'y': -1}
	reverseSpawn = 0
	
	numOfRedPickUp = 0
	numOfGreenPickUp = 0
	numOfBluePickUp = 0
	time = 2000
	negativeMessage = "Not Obtained"
	reverseMessage = "Not Obtained"
	negative = False
	reverse = False
	
	redPickUp1 = getRandomLocation()
	redPickUp2 = getRandomLocation()
	redPickUp3 = getRandomLocation()
	redPickUp4 = getRandomLocation()
	redPickUp5 = getRandomLocation()
	greenPickUp1 = getRandomLocation()
	greenPickUp2 = getRandomLocation()
	greenPickUp3 = getRandomLocation()
	greenPickUp4 = getRandomLocation()
	greenPickUp5 = getRandomLocation()
	bluePickUp1 = getRandomLocation()
	bluePickUp2 = getRandomLocation()
	bluePickUp3 = getRandomLocation()
	bluePickUp4 = getRandomLocation()
	bluePickUp5 = getRandomLocation()
	
	while True:
		negativeSpawnChance = random.randint(0, 750)
		reverseSpawnChance = random.randint(0, 750)
	
		playerMove = None
		keyPressed = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				stop()
			elif event.type == KEYDOWN:
				keyPressed = True
				if (event.key == K_LEFT and playerLocation['x'] != 0):
					playerMove = LEFT
				elif (event.key == K_RIGHT and playerLocation['x'] != 19):
					playerMove = RIGHT
				elif (event.key == K_UP and playerLocation['y'] != 0):
					playerMove = UP
				elif (event.key == K_DOWN and playerLocation['y'] != 14):
					playerMove = DOWN
					
		if playerMove == UP:
			playerLocation = {'x': playerLocation['x'], 'y': playerLocation['y'] - 1}
		elif playerMove == DOWN:
			playerLocation = {'x': playerLocation['x'], 'y': playerLocation['y'] + 1}
		elif playerMove == LEFT:
			playerLocation = {'x': playerLocation['x'] - 1, 'y': playerLocation['y']}
		elif playerMove == RIGHT:
			playerLocation = {'x': playerLocation['x'] + 1, 'y': playerLocation['y']}
			
		if (playerLocation['x'] == redPickUp1['x'] and playerLocation['y'] == redPickUp1['y']):
			redPickUp1 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp2['x'] and playerLocation['y'] == redPickUp2['y']):
			redPickUp2 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp3['x'] and playerLocation['y'] == redPickUp3['y']):
			redPickUp3 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp4['x'] and playerLocation['y'] == redPickUp4['y']):
			redPickUp4 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp5['x'] and playerLocation['y'] == redPickUp5['y']):
			redPickUp5 = getRandomLocation()
			numOfRedPickUp += 1
			
		if (playerLocation['x'] == bluePickUp1['x'] and playerLocation['y'] == bluePickUp1['y']):
			bluePickUp1 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp2['x'] and playerLocation['y'] == bluePickUp2['y']):
			bluePickUp2 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp3['x'] and playerLocation['y'] == bluePickUp3['y']):
			bluePickUp3 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp4['x'] and playerLocation['y'] == bluePickUp4['y']):
			bluePickUp4 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp5['x'] and playerLocation['y'] == bluePickUp5['y']):
			bluePickUp5 = getRandomLocation()
			numOfBluePickUp += 1
			
		if (playerLocation['x'] == greenPickUp1['x'] and playerLocation['y'] == greenPickUp1['y']):
			greenPickUp1 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp2['x'] and playerLocation['y'] == greenPickUp2['y']):
			greenPickUp2 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp3['x'] and playerLocation['y'] == greenPickUp3['y']):
			greenPickUp3 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp4['x'] and playerLocation['y'] == greenPickUp4['y']):
			greenPickUp4 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp5['x'] and playerLocation['y'] == greenPickUp5['y']):
			greenPickUp5 = getRandomLocation()
			numOfGreenPickUp += 1
			
		if (playerLocation['x'] == negativeLocation['x'] and playerLocation['y'] == negativeLocation['y']):
			negativeMessage = "Obtained!"
			negative = True
			removeNegativePickUp(negativeLocation)
			
		if (playerLocation['x'] == reverseLocation['x'] and playerLocation['y'] == reverseLocation['y']):
			reverseMessage = "Obtained!"
			reverse = True
			removeReversePickUp(reverseLocation)
			
			
		
		if keyPressed == True:
			drawPlayer(playerLocation)
		
		GAMEWINDOW.fill(BACKGROUNDCOLOR)
		drawTiles()
		drawPlayer(playerLocation)
		
		drawRedPickUp(redPickUp1)
		drawRedPickUp(redPickUp2)
		drawRedPickUp(redPickUp3)
		drawRedPickUp(redPickUp4)
		drawRedPickUp(redPickUp5)
		
		drawGreenPickUp(greenPickUp1)
		drawGreenPickUp(greenPickUp2)
		drawGreenPickUp(greenPickUp3)
		drawGreenPickUp(greenPickUp4)
		drawGreenPickUp(greenPickUp5)
		
		drawBluePickUp(bluePickUp1)
		drawBluePickUp(bluePickUp2)
		drawBluePickUp(bluePickUp3)
		drawBluePickUp(bluePickUp4)
		drawBluePickUp(bluePickUp5)
		
		if (negativeSpawnChance == 375 and negativeSpawn == 0):
			negativeLocation = getRandomLocation()
			negativeSpawn = 1
			
		if (reverseSpawnChance == 375 and reverseSpawn == 0):
			reverseLocation = getRandomLocation()
			reverseSpawn = 1
			
		if (negativeMessage == "Not Obtained"):
			drawNegativePickUp(negativeLocation)
			
		if (reverseMessage == "Not Obtained"):
			drawReversePickUp(reverseLocation)
		
		time -= 1
		
		displayCollection(numOfRedPickUp, numOfGreenPickUp, numOfBluePickUp, time, negativeMessage, reverseMessage)
		
		if (time == 0):
			stop() # will change later to start image changer thingy
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
					
				
	
	
	
def stop():
	pygame.quit()
	sys.exit()
	
def displayCollection(numOfRedPickUp, numOfGreenPickUp, numOfBluePickUp, time, negativeMessage, reverseMessage):
	collectionBoxRed = BASICFONT.render("Red Pick-Ups: %s" % (numOfRedPickUp), True, WHITE)
	redBoxRect = collectionBoxRed.get_rect()
	redBoxRect.topright = (GAMEWIDTH - 25, 10)
	GAMEWINDOW.blit(collectionBoxRed, redBoxRect)\
	
	collectionBoxGreen = BASICFONT.render("Green Pick-Ups: %s" % (numOfGreenPickUp), True, WHITE)
	greenBoxRect = collectionBoxGreen.get_rect()
	greenBoxRect.topright = (GAMEWIDTH - 25, 30)
	GAMEWINDOW.blit(collectionBoxGreen, greenBoxRect)
	
	collectionBoxBlue = BASICFONT.render("Blue Pick-Ups: %s" % (numOfBluePickUp), True, WHITE)
	blueBoxRect = collectionBoxBlue.get_rect()
	blueBoxRect.topright = (GAMEWIDTH - 25, 50)
	GAMEWINDOW.blit(collectionBoxBlue, blueBoxRect)
	
	collectionBoxTime = BASICFONT.render("Time: %s" % (time), True, WHITE)
	timeBoxRect = collectionBoxTime.get_rect()
	timeBoxRect.topright = (GAMEWIDTH - 25, 110)
	GAMEWINDOW.blit(collectionBoxTime, timeBoxRect)
	
	collectionBoxNegative = BASICFONT.render("Negative: %s" % (negativeMessage), True, WHITE)
	negativeBoxRect = collectionBoxNegative.get_rect()
	negativeBoxRect.topright = (GAMEWIDTH - 25, 70)
	GAMEWINDOW.blit(collectionBoxNegative, negativeBoxRect)
	
	collectionBoxReverse = BASICFONT.render("Reverse: %s" % (reverseMessage), True, WHITE)
	reverseBoxRect = collectionBoxReverse.get_rect()
	reverseBoxRect.topright = (GAMEWIDTH - 25, 90)
	GAMEWINDOW.blit(collectionBoxReverse, reverseBoxRect)
	
def getRandomLocation():	
	return {'x': random.randint(0,TILEWIDTH - 1), 'y': random.randint(0,TILEHEIGHT - 1)}
	
def drawRedPickUp(redPickUpLocation):
	x = redPickUpLocation['x'] * TILESIZE
	y = redPickUpLocation['y'] * TILESIZE
	redPickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, RED, redPickUpParticle)
	
def drawGreenPickUp(greenPickUpLocation):
	x = greenPickUpLocation['x'] * TILESIZE
	y = greenPickUpLocation['y'] * TILESIZE
	greenPickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, GREEN, greenPickUpParticle)
	
def drawBluePickUp(bluePickUpLocation):
	x = bluePickUpLocation['x'] * TILESIZE
	y = bluePickUpLocation['y'] * TILESIZE
	bluePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLUE, bluePickUpParticle)
	
def drawNegativePickUp(negativeLocation):
	x = negativeLocation['x'] * TILESIZE
	y = negativeLocation['y'] * TILESIZE
	negativePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, WHITE, negativePickUpParticle)
	
def removeNegativePickUp(negativeLocation):
	x = negativeLocation['x'] * TILESIZE
	y = negativeLocation['y'] * TILESIZE
	negativePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLACK, negativePickUpParticle)
	
def drawReversePickUp(reverseLocation):
	x = reverseLocation['x'] * TILESIZE
	y = reverseLocation['y'] * TILESIZE
	reversePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, PURPLE, reversePickUpParticle)
	
def removeReversePickUp(reverseLocation):
	x = reverseLocation['x'] * TILESIZE
	y = reverseLocation['y'] * TILESIZE
	reversePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLACK, reversePickUpParticle)
	
def drawPlayer(playerLocation):
	x = playerLocation['x'] * TILESIZE	
	y = playerLocation['y'] * TILESIZE
	playerOuterShell = pygame.Rect(x + 1, y + 1, TILESIZE - 1, TILESIZE - 1)
	pygame.draw.rect(GAMEWINDOW, DARKORANGE, playerOuterShell)
	playerInnerShell = pygame.Rect(x + 7, y + 7, TILESIZE - 13, TILESIZE - 13)
	pygame.draw.rect(GAMEWINDOW, ORANGE, playerInnerShell)
	
def drawTiles():
	for x in range(0, GAMEWIDTH, TILESIZE):
		pygame.draw.line(GAMEWINDOW, WHITE, (x, 0), (x, GAMEHEIGHT))
	for y in range(0, GAMEHEIGHT, TILESIZE):
		pygame.draw.line(GAMEWINDOW, WHITE, (0, y), (GAMEWIDTH, y))
		
if __name__ == '__main__':
	main() 
