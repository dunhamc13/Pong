# Program by Christian Dunham 21 August 2019
# This is a class game of pong.  The game inherits functionality from graphics.py
# The structure of the game is centered on the main function (a menu to let the user -
# select whether they want to play a 2 player game against another human, or a 1 player
# game against a computer.

# The program is futher structured with basic classes for a ball and paddle.  There are 
# several auxilliary functions to assist making the game more realistic or to ease programming
# such as several random generators using algorithms to increase CP(computer player) 
# realism, or a message generator to simplify the graphics.py text object production.

# Additional logic was added into each game type such as slowly increasing ball speed
# and decreasing paddle widths as the game play continues  Finally, extensive nested 
# While loops were used to animate text during game play and to ease user experince 
# toggling back and forth between games all windows were passed through to each other.... 

from graphics import *
from random import *
import random 


###########################################################################################
###############                  Menus                          ###########################
###########################################################################################


#menu for program start
def startMenu():

    #menu variables
    WindowX = 400
    WindowY = 200

    #create menu
    menuWindow = GraphWin("Pong", WindowX, WindowY)
    menuWindow.setBackground("black")

                            
    #create menu and get selection
    optionsText = Text(Point(200,100), "##########################\n########## PONG ##########\n##########################\n\nOne Player Game : press 1 :  \n\nTwo Player Game : press 2 :  \n\nQuit : press 3 :  ")
    optionsText.setTextColor("white")
    optionsText.draw(menuWindow)

    #check user wishes, give instructions and pass into game types
    while True:
        userSelection = menuWindow.checkKey()

        if userSelection == '1':
            optionsText.undraw()

            instructions = messageGenerator("##########################\n########## PONG ##########\n\n'W' to move up\n\n'S' to move down\n\nFirst to 11 wins\n\nQ to return to menu")
            instructions.draw(menuWindow)
            i = 0
            while i < 6000:
                i+=1
                instructions.setTextColor("white")
            instructions.undraw()
            onePlayerGame(menuWindow)

        elif userSelection == '2':
            optionsText.undraw()
            instructions = messageGenerator("##########################\n########## PONG ##########\n\n'W' or 'I' to move up\n\n'S' or 'K' to move down\n\nFirst to 11 wins\n\nQ to return to menu")
            instructions.setSize(11)
            instructions.draw(menuWindow)
            i = 0
            while i < 6000:
                i+=1
                instructions.setTextColor("white")
            instructions.undraw()
            Main(menuWindow)


        elif userSelection == '3':

            optionsText.undraw()
            i = 0
            goodBye = Text(Point(200,100), "Thanks for playing!")
            goodBye.draw(menuWindow)
            while i < 6000:
                i+=1
                goodBye.setTextColor("white")
            goodBye.undraw()

            menuWindow.close()
            sys.exit(0)

#menu for program
def menu(graphWindow):

    #menu variables
    WindowX = 400
    WindowY = 200

    #create menu
    menuWindow = graphWindow
    menuWindow.setBackground("black")

                            
    #create menu and get selection
    optionsText = Text(Point(200,100), "##########################\n########## PONG ##########\n##########################\n\nOne Player Game : press 1 :  \n\nTwo Player Game : press 2 :  \n\nQuit : press 3 : ")
    optionsText.setTextColor("white")
    optionsText.draw(menuWindow)

    #check user wishes
    while True:
        userSelection = menuWindow.checkKey()

        if userSelection == '1':
            optionsText.undraw()
            instructions = messageGenerator("##########################\n########## PONG ##########\n\n'W' to move up\n\n'S' to move down\n\nFirst to 11 wins\n\nQ to return to menu")
            instructions.draw(menuWindow)
            i = 0
            while i < 6000:
                i+=1
                instructions.setTextColor("white")
            instructions.undraw()
            onePlayerGame(menuWindow)

        elif userSelection == '2':
            optionsText.undraw()
            instructions = messageGenerator("##########################\n########## PONG ##########\n\n'W' or 'I' to move up\n\n'S' or 'K' to move down\n\nFirst to 11 wins\n\nQ to return to menu")
            instructions.setSize(11)
            instructions.draw(menuWindow)
            i = 0
            while i < 6000:
                i+=1
                instructions.setTextColor("white")
            instructions.undraw()
            Main(menuWindow)


        elif userSelection == '3':

            optionsText.undraw()
            i = 0
            goodBye = Text(Point(200,100), "Thanks for playing!")
            goodBye.draw(menuWindow)
            while i < 6000:
                i+=1
                goodBye.setTextColor("white")
            goodBye.undraw()

            menuWindow.close()
            sys.exit(0)


############################################################################################
###############                 Randomization                    ###########################
############################################################################################



#create random number for where to set the ball on y axis
def randomNumber():
    number = random.randint(25,175)
    return number


#create random number for how often cpu loses concentration
def randomHowOften():
    number = random.randint(2850,3850)
    return number

#create random number for how long cpu loses concentration
def randomHowLong():
    number = random.randint(800,1700)
    return number

#create random up response for cpu
def randomUpCPU():

    #create dictionary of responses
    upDict = {1:0, 2:1, 3:1, 4:1, 5:0}
    number = random.randint(1,5)
    response = upDict[number]
    return response

#create random down response for cpu
def randomDownCPU():

    #create dictionary of responses
    upDict = {1:0, 2:-1, 3:-1, 4:-1, 5:0}
    number = random.randint(1,5)
    response = upDict[number]
    return response




###########################################################################################
###############                  Classes                        ###########################
###########################################################################################
###############             & Support Functions                  ##########################
###########################################################################################



#class to create balls
class Ball(Circle):

    #make a random int for y axis
    number = randomNumber()

    #object constructor with argument for ball size
    def __init__(self, ballSize, number):
        self.ballSize = ballSize
        self.centerPointX = 200
        self.centerPointY = number
        self.Fill = 'yellow'
        self.OutLine = 'Black'        

#function to make a pong ball
def makeBall(ball):

        #create a pongball from circle
        pongBall = Circle(Point(ball.centerPointX, ball.centerPointY), ball.ballSize)
        pongBall.setFill(ball.Fill)
        pongBall.setOutline(ball.OutLine)
        return pongBall
    
#class to create paddles
class Paddle(Rectangle):
    
    #object constructor with argument for paddles
    def __init__(self, paddleXSize, paddleYSize, fill, outline):
            self.PaddleXSize = paddleXSize
            self.PaddleYSize = paddleYSize
            self.Fill = fill
            self.Outline = outline

#function to make left paddle
def makeLeftPaddle(leftPaddle, WindowY):

        #create a paddle from rectangle
        paddle = Rectangle(Point(5, WindowY / 2 - leftPaddle.PaddleYSize / 2), Point(leftPaddle.PaddleXSize + 5, WindowY / 2 + leftPaddle.PaddleYSize / 2))
        paddle.setFill(leftPaddle.Fill)
        paddle.setOutline(leftPaddle.Outline)
        return paddle

#function to make right paddle
def makeRightPaddle(rightPaddle, WindowX, WindowY):

        #create a paddle from rectangle
        paddle = Rectangle(Point(WindowX - 5, WindowY / 2 - rightPaddle.PaddleYSize / 2), Point(WindowX - rightPaddle.PaddleXSize - 5, WindowY / 2 + rightPaddle.PaddleYSize / 2))
        paddle.setFill(rightPaddle.Fill)
        paddle.setOutline(rightPaddle.Outline)
        return paddle
    
#function to make messages
def messageGenerator(text):
    
        #make strings to put together to make a message for Text
        message = Text(Point(200,100), text)
        return message



###########################################################################################
################            Main Functions for Game Types           #######################
###########################################################################################



#play a second round that's harder
def onePlayerGame(graphWindow):

    #variables for the game
    WindowX = 400
    WindowY = 200
    xSpeed = .045
    ySpeed = .045
    PaddleXSize = 5
    PaddleYSize = 40
    ballSize = 5

    #variables for score
    P1_Counter = 0
    P1_one = Text(Point(5,8),"1")
    P1_one.setTextColor("white")
    P1_two = Text(Point(5,8),"2")
    P1_two.setTextColor("white")
    P1_three = Text(Point(5,8),"3")
    P1_three.setTextColor("white")
    P1_four = Text(Point(5,8),"4")
    P1_four.setTextColor("white")
    P1_five = Text(Point(5,8),"5")
    P1_five.setTextColor("white")
    P1_six = Text(Point(5,8),"6")
    P1_six.setTextColor("white")
    P1_seven = Text(Point(5,8),"7")
    P1_seven.setTextColor("white")
    P1_eight = Text(Point(5,8),"8")
    P1_eight.setTextColor("white")
    P1_nine = Text(Point(5,8),"9")
    P1_nine.setTextColor("white")
    P1_ten = Text(Point(8,8),"10")
    P1_ten.setTextColor("white")
    P1_eleven = Text(Point(200,100),"WINNER")
    P1_eleven.setTextColor("white")
    P2_Counter = 0
    P2_one = Text(Point(390,8),"1")
    P2_one.setTextColor("white")
    P2_two = Text(Point(390,8),"2")
    P2_two.setTextColor("white")
    P2_three = Text(Point(390,8),"3")
    P2_three.setTextColor("white")
    P2_four = Text(Point(390,8),"4")
    P2_four.setTextColor("white")
    P2_five = Text(Point(390,8),"5")
    P2_five.setTextColor("white")
    P2_six = Text(Point(390,8),"6")
    P2_six.setTextColor("white")
    P2_seven = Text(Point(390,8),"7")
    P2_seven.setTextColor("white")
    P2_eight = Text(Point(390,8),"8")
    P2_eight.setTextColor("white")
    P2_nine = Text(Point(390,8),"9")
    P2_nine.setTextColor("white")
    P2_ten = Text(Point(390,8),"10")
    P2_ten.setTextColor("white")
    P2_eleven = Text(Point(200,100),"WINNER")
    P2_eleven.setTextColor("white")

    #make a game window
    gameWindowLevelII = graphWindow

    #make a pong ball
    number = randomNumber()
    aBall = Ball(ballSize, number)
    pongBall = makeBall(aBall)
    pongBall.draw(gameWindowLevelII)


    #make a left paddle
    lPaddle = Paddle( PaddleXSize, PaddleYSize, 'blue', 'black')
    leftPaddle = makeLeftPaddle(lPaddle, WindowY)
    leftPaddle.draw(gameWindowLevelII)

    #make a right paddle
    rPaddle = Paddle( PaddleXSize, PaddleYSize-.5, 'red', 'black')
    rightPaddle = makeRightPaddle(rPaddle, WindowX, WindowY)
    rightPaddle.draw(gameWindowLevelII)

    #function for score screen message
    def score(color):
                        #animate score on screen
                text = "Score " + color + " Team!!!"
                i = 0
                message = messageGenerator(text)
                message.draw(gameWindowLevelII)
                while i < 1500:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 3
                i = 0
                message = messageGenerator("3")
                message.draw(gameWindowLevelII)
                while i < 1200:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 2
                i = 0
                message = messageGenerator("2")
                message.draw(gameWindowLevelII)
                while i < 1000:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 1
                i = 0
                message = messageGenerator("1")
                message.draw(gameWindowLevelII)
                while i < 800:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate Serve
                i = 0
                message = messageGenerator("Serve!")
                message.draw(gameWindowLevelII)
                while i < 600:
                    i+=1
                    message.setTextColor(color)
                message.undraw()



    #variables for computer concentration
    howOftenBreakCounter = 2000
    howLongBreakCounter = 0

    #While loop to animate the game 
    while True:

        #check keys for up and down que from user
        movePaddle = gameWindowLevelII.checkKey()
        
        #if statement to move the user paddle up and down
        if movePaddle == 'w':
            leftPaddle.move(0,-10)
        elif movePaddle == 's':
            leftPaddle.move(0,10)
        elif movePaddle == 't':
            xSpeed += .0025
            ySpeed += .0025
        elif movePaddle == 'y':
            xSpeed -= .0025
            ySpeed -= .0025
        elif movePaddle == 'q':
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindowLevelII)

        if howOftenBreakCounter == 0:
            howLongBreakCounter = randomHowLong()
            howOftenBreakCounter = -1
            #print("Start Break")
        else:
            howOftenBreakCounter -=1
            #print(howOftenBreakCounter)

        #print(howLongBreakCounter)
        if howLongBreakCounter <= 0:
            #move CPU up
            if pongBall.getCenter().getY() > rightPaddle.getCenter().getY() + PaddleYSize / 4 and pongBall.getCenter().getX() > 200 and xSpeed > 0:

                #get computer response            
                #cpuResponse = randomUpCPU()
                rightPaddle.move(0,1)

            #move CPU down
            if pongBall.getCenter().getY() < rightPaddle.getCenter().getY() - PaddleYSize / 4 and pongBall.getCenter().getX() > 200 and xSpeed > 0:

                #get computer response
               #cpuResponse = randomDownCPU()
                rightPaddle.move(0, -1)
        else:
            howLongBreakCounter -= 1

        if howLongBreakCounter <= 0 and howOftenBreakCounter < 0:
            howOftenBreakCounter = randomHowOften()

        if xSpeed < 0 and pongBall.getCenter().getX() > 200 and rightPaddle.getCenter().getY() < 100 :
            rightPaddle.move(0, .5)

        if xSpeed < 0 and pongBall.getCenter().getX() > 200 and rightPaddle.getCenter().getY() > 101 :
            rightPaddle.move(0, -.5)

         #if ball goes beyond right side of screen

        if pongBall.getCenter().getX() > WindowX - ballSize:
            #remove ball update speed
            pongBall.undraw()

            #counter for score
            P2_Counter += 1

            #if blue team score 1
            if P2_Counter == 1:
                xSpeed = .05
                ySpeed = .05
                P2_one.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 2
            if P2_Counter == 2:
                xSpeed = .055
                ySpeed = .055
                P2_one.undraw()
                P2_two.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if score 3 red team
            if P2_Counter == 3:
                P2_two.undraw()
                xSpeed = .057
                ySpeed = .057
                P2_three.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 4
            if P2_Counter == 4:
                P2_three.undraw()
                xSpeed = .059
                ySpeed = .059
                P2_four.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 5
            if P2_Counter == 5:
                P2_four.undraw()
                xSpeed = .06
                ySpeed = .06
                P2_five.draw(gameWindowLevelII)     
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 6
            if P2_Counter == 6:
                P2_five.undraw()
                xSpeed = .062
                ySpeed = .062
                P2_six.draw(gameWindowLevelII)
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 7
            if P2_Counter == 7:
                P2_six.undraw()
                xSpeed = .064
                ySpeed = .064
                P2_seven.draw(gameWindowLevelII)
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 8
            if P2_Counter == 8:
                P2_seven.undraw()
                xSpeed = .066
                ySpeed = .066
                P2_eight.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 9
            if P2_Counter == 9:
                P2_eight.undraw()
                xSpeed = .068
                ySpeed = .068
                P2_nine.draw(gameWindowLevelII)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 10
            if P2_Counter == 10:
                P2_nine.undraw()
                xSpeed = .071
                ySpeed = .071
                P2_ten.draw(gameWindowLevelII)     
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 11
            if P2_Counter == 11:
                P2_eleven.draw(gameWindowLevelII)
                P2_eleven.move(xSpeed,ySpeed)
                P2_eleven.undraw()

                #animate Win
                i = 0
                message = messageGenerator("Blue Team Wins!!!!")
                message.draw(gameWindowLevelII)
                while i < 1500:
                    i+=1
                    message.setTextColor("Blue")
                message.undraw()

                #create menu
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindowLevelII)

            #set ball to serve from red to blue
            xSpeed  = xSpeed + .0025 
            ySpeed = ySpeed + .00025

        #if ball goes beyond right side of screen
        if pongBall.getCenter().getX() < ballSize:

            #remove ball update speed
            pongBall.undraw()
            xSpeed = xSpeed + .005
            ySpeed = ySpeed + .005

            #counter for score
            P1_Counter += 1

            #if red team score 1
            if P1_Counter == 1:
                xSpeed = -.055
                ySpeed = -.055
                P1_one.draw(gameWindowLevelII)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 2
            if P1_Counter == 2:
                xSpeed = -.057
                ySpeed = -.057
                P1_one.undraw()
                P1_two.draw(gameWindowLevelII)

                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if score 3 red team
            if P1_Counter == 3:
                P1_two.undraw()
                xSpeed = -.059
                ySpeed = -.059
                P1_three.draw(gameWindowLevelII)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 4
            if P1_Counter == 4:
                P1_three.undraw()
                xSpeed = -.06
                ySpeed = -.06
                P1_four.draw(gameWindowLevelII)
                
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 5
            if P1_Counter == 5:
                P1_four.undraw()
                xSpeed = -.062
                ySpeed = -.062
                P1_five.draw(gameWindowLevelII)     
                score("Red")
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 6
            if P1_Counter == 6:
                P1_five.undraw()
                P1_six.draw(gameWindowLevelII)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 7
            if P1_Counter == 7:
                P1_six.undraw()
                xSpeed = -.064
                ySpeed = -.064
                P1_seven.draw(gameWindowLevelII)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 8
            if P1_Counter == 8:
                P1_seven.undraw()
                xSpeed = -.066
                ySpeed = -.066
                P1_eight.draw(gameWindowLevelII)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)
                
            #if red team score 9
            if P1_Counter == 9:
                P1_eight.undraw()
                xSpeed = -.068
                ySpeed = -.068
                P1_nine.draw(gameWindowLevelII)
                score("Red")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 10
            if P1_Counter == 10:
                P1_nine.undraw()
                xSpeed = -.072
                ySpeed = -.072
                P1_ten.draw(gameWindowLevelII)     
                score("Red")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindowLevelII)

            #if red team score 11
            if P1_Counter == 11:
                P1_eleven.draw(gameWindowLevelII)
                P1_eleven.move(xSpeed,ySpeed)
                P1_eleven.undraw()

                #animate Win
                i = 0
                message = messageGenerator("Red Team Wins!!!!")
                message.draw(gameWindowLevelII) 
                while i < 1500:
                    i+=1
                    message.setTextColor("Red")
                message.undraw()

                #create menu
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindowLevelII)


        if pongBall.getCenter().getY() > WindowY - ballSize:
                        #set ball to serve from red to blue 
            ySpeed = -ySpeed 
                 #if ball goes beyond right side of screen
        if pongBall.getCenter().getY() < ballSize:
                        #set ball to serve from red to blue
            ySpeed  = -ySpeed

        #if statements to detect paddle collision with ball with right paddle
        if pongBall.getCenter().getX() > rightPaddle.getCenter().getX() - PaddleXSize / 2 and pongBall.getCenter().getY() < (rightPaddle.getCenter().getY() + PaddleYSize / 2) and pongBall.getCenter().getY() > (rightPaddle.getCenter().getY() - PaddleYSize / 2) : 


            ySpeed = -ySpeed 
            xSpeed = -xSpeed 

        #if statements to detect paddle collision with ball left paddle
        if pongBall.getCenter().getX() < leftPaddle.getCenter().getX() + PaddleXSize / 2 and pongBall.getCenter().getY() < (leftPaddle.getCenter().getY() + PaddleYSize / 2) and pongBall.getCenter().getY() > (leftPaddle.getCenter().getY() - PaddleYSize / 2) : 

            ySpeed = -ySpeed 
            xSpeed = -xSpeed 


        pongBall.move(xSpeed,ySpeed)
             
          


###########################################################################################
################         Main Function for 2 Player Game       ############################
###########################################################################################


#main function - this is for 2 player game
def Main(graphWindow):
    
    #variables for the game
    WindowX = 400
    WindowY = 200
    xSpeed = .04
    ySpeed = .04
    PaddleXSize = 5
    PaddleYSize = 40
    ballSize = 5

    #variables for score
    P1_Counter = 0
    P1_one = Text(Point(5,8),"1")
    P1_one.setTextColor("white")
    P1_two = Text(Point(5,8),"2")
    P1_two.setTextColor("white")
    P1_three = Text(Point(5,8),"3")
    P1_three.setTextColor("white")
    P1_four = Text(Point(5,8),"4")
    P1_four.setTextColor("white")
    P1_five = Text(Point(5,8),"5")
    P1_five.setTextColor("white")
    P1_six = Text(Point(5,8),"6")
    P1_six.setTextColor("white")
    P1_seven = Text(Point(5,8),"7")
    P1_seven.setTextColor("white")
    P1_eight = Text(Point(5,8),"8")
    P1_eight.setTextColor("white")
    P1_nine = Text(Point(5,8),"9")
    P1_nine.setTextColor("white")
    P1_ten = Text(Point(8,8),"10")
    P1_ten.setTextColor("white")
    P1_eleven = Text(Point(200,100),"WINNER")
    P1_eleven.setTextColor("white")
    P2_Counter = 0
    P2_one = Text(Point(390,8),"1")
    P2_one.setTextColor("white")
    P2_two = Text(Point(390,8),"2")
    P2_two.setTextColor("white")
    P2_three = Text(Point(390,8),"3")
    P2_three.setTextColor("white")
    P2_four = Text(Point(390,8),"4")
    P2_four.setTextColor("white")
    P2_five = Text(Point(390,8),"5")
    P2_five.setTextColor("white")
    P2_six = Text(Point(390,8),"6")
    P2_six.setTextColor("white")
    P2_seven = Text(Point(390,8),"7")
    P2_seven.setTextColor("white")
    P2_eight = Text(Point(390,8),"8")
    P2_eight.setTextColor("white")
    P2_nine = Text(Point(390,8),"9")
    P2_nine.setTextColor("white")
    P2_ten = Text(Point(390,8),"10")
    P2_ten.setTextColor("white")
    P2_eleven = Text(Point(200,100),"WINNER")
    P2_eleven.setTextColor("white")

    #make a game window
    gameWindow = graphWindow

    #make a pong ball
    number = randomNumber()
    aBall = Ball(ballSize, number)
    pongBall = makeBall(aBall)
    pongBall.draw(gameWindow)


    #make a left paddle
    lPaddle = Paddle( PaddleXSize, PaddleYSize, 'blue', 'black')
    leftPaddle = makeLeftPaddle(lPaddle, WindowY)
    leftPaddle.draw(gameWindow)

    #make a right paddle
    rPaddle = Paddle( PaddleXSize, PaddleYSize, 'red', 'black')
    rightPaddle = makeRightPaddle(rPaddle, WindowX, WindowY)
    rightPaddle.draw(gameWindow)

    
    #function for score screen message
    def score(color):
                        #animate score on screen
                text = "Score " + color + " Team!!!"
                i = 0
                message = messageGenerator(text)
                message.draw(gameWindow)
                while i < 1500:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 3
                i = 0
                message = messageGenerator("3")
                message.draw(gameWindow)
                while i < 1200:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 2
                i = 0
                message = messageGenerator("2")
                message.draw(gameWindow)
                while i < 1000:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate 1
                i = 0
                message = messageGenerator("1")
                message.draw(gameWindow)
                while i < 800:
                    i+=1
                    message.setTextColor("white")
                message.undraw()

                #animate Serve
                i = 0
                message = messageGenerator("Serve!")
                message.draw(gameWindow)
                while i < 600:
                    i+=1
                    message.setTextColor(color)
                message.undraw()


    #While loop to animate the game 
    while True:

        #check keys for up and down que from user
        movePaddle = gameWindow.checkKey()
        
        #if statement to move the user paddle up and down
        if movePaddle == 'w':
            leftPaddle.move(0,-10)
        elif movePaddle == 's':
            leftPaddle.move(0,10)
        elif movePaddle == 'i':
            rightPaddle.move(0,-10)
        elif movePaddle == 'k':
            rightPaddle.move(0,10)
        elif movePaddle == 'q':
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindow)
       

    
        #if ball goes beyond right side of screen
        if pongBall.getCenter().getX() > WindowX - ballSize:
            #remove ball update speed
            pongBall.undraw()

            #counter for score
            P2_Counter += 1

            #if red team score 1
            if P2_Counter == 1:
                xSpeed = .045
                ySpeed = .045
                P2_one.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 2
            if P2_Counter == 2:
                P2_one.undraw()
                xSpeed = .05
                ySpeed = .05
                P2_two.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if score 3 red team
            if P2_Counter == 3:
                P2_two.undraw()
                xSpeed = .055
                ySpeed = .055
                P2_three.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 4
            if P2_Counter == 4:
                xSpeed = .06
                ySpeed = .06
                P2_three.undraw()
                P2_four.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 5
            if P2_Counter == 5:
                xSpeed = .063
                ySpeed = .063
                P2_four.undraw()
                P2_five.draw(gameWindow)     
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 6
            if P2_Counter == 6:
                P2_five.undraw()
                xSpeed = .065
                ySpeed = .065
                P2_six.draw(gameWindow)
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 7
            if P2_Counter == 7:
                P2_six.undraw()
                xSpeed = .067
                ySpeed = .067
                P2_seven.draw(gameWindow)
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 8
            if P2_Counter == 8:
                P2_seven.undraw()
                xSpeed = .069
                ySpeed = .069
                P2_eight.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 9
            if P2_Counter == 9:
                xSpeed = .071
                ySpeed = .071
                P2_eight.undraw()
                P2_nine.draw(gameWindow)
                score("Blue")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 10
            if P2_Counter == 10:
                P2_nine.undraw()
                xSpeed = .073
                ySpeed = .073
                P2_ten.draw(gameWindow)     
                score("Blue")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 11
            if P2_Counter == 11:
                P2_eleven.draw(gameWindow)
                P2_eleven.move(xSpeed,ySpeed)
                P2_eleven.undraw()

                #animate Win
                i = 0
                message = messageGenerator("Blue Team Wins!!!!")
                message.draw(gameWindow)
                while i < 1500:
                    i+=1
                    message.setTextColor("blue")
                message.undraw()

                #create menu
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindow)

        #if ball goes beyond left side of screen
        if pongBall.getCenter().getX() < ballSize:
            #remove ball update speed
            pongBall.undraw()


            #counter for score
            P1_Counter += 1

            #if red team score 1
            if P1_Counter == 1:
                xSpeed = -.045
                ySpeed = -.045
                P1_one.draw(gameWindow)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 2
            if P1_Counter == 2:
                P1_one.undraw()
                xSpeed = -.05
                ySpeed = -.05
                P1_two.draw(gameWindow)

                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if score 3 red team
            if P1_Counter == 3:
                P1_two.undraw()
                xSpeed = -.055
                ySpeed = -.055
                P1_three.draw(gameWindow)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 4
            if P1_Counter == 4:
                P1_three.undraw()
                xSpeed = -.06
                ySpeed = -.06
                P1_four.draw(gameWindow)
                
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 5
            if P1_Counter == 5:
                P1_four.undraw()
                xSpeed = -.063
                ySpeed = -.063
                P1_five.draw(gameWindow)     
                score("Red")
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 6
            if P1_Counter == 6:
                P1_five.undraw()
                xSpeed = -.065
                ySpeed = -.065
                P1_six.draw(gameWindow)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 7
            if P1_Counter == 7:
                P1_six.undraw()
                xSpeed = -.067
                ySpeed = -.067
                P1_seven.draw(gameWindow)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 8
            if P1_Counter == 8:
                P1_seven.undraw()
                xSpeed = -.069
                ySpeed = -.069
                P1_eight.draw(gameWindow)
                score("Red")

                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)
                
            #if red team score 9
            if P1_Counter == 9:
                P1_eight.undraw()
                xSpeed = -.071
                ySpeed = -.071
                P1_nine.draw(gameWindow)
                score("Red")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 10
            if P1_Counter == 10:
                P1_nine.undraw()
                xSpeed = -.073
                ySpeed = -.073
                P1_ten.draw(gameWindow)     
                score("Red")
                
                #make a pong ball
                number = randomNumber()
                aBall = Ball(ballSize, number)
                pongBall = makeBall(aBall)
                pongBall.draw(gameWindow)

            #if red team score 11
            if P1_Counter == 11:
                P1_eleven.draw(gameWindow)
                P1_eleven.move(xSpeed,ySpeed)
                P1_eleven.undraw()

                #animate Win
                i = 0
                message = messageGenerator("Red Team Wins!!!!")
                message.draw(gameWindow) 
                while i < 1500:
                    i+=1
                    message.setTextColor("red")
                message.undraw()

                #create menu
                P1_one.undraw()
                P1_two.undraw()
                P1_three.undraw()
                P1_four.undraw()
                P1_five.undraw()
                P1_six.undraw()
                P1_seven.undraw()
                P1_eight.undraw()
                P1_nine.undraw()
                P1_ten.undraw()
                P1_eleven.undraw()
                P2_one.undraw()
                P2_one.undraw()
                P2_two.undraw()
                P2_three.undraw()
                P2_four.undraw()
                P2_five.undraw()
                P2_six.undraw()
                P2_seven.undraw()
                P2_eight.undraw()
                P2_nine.undraw()
                P2_ten.undraw()
                P2_eleven.undraw()
                pongBall.undraw()
                rightPaddle.undraw()
                leftPaddle.undraw()
                menu(gameWindow)

        #if ball goes to high
        if pongBall.getCenter().getY() > WindowY - ballSize:
            ySpeed = -ySpeed

        #if ball boes to low
        if pongBall.getCenter().getY() < ballSize:
            ySpeed = -ySpeed

        #if statements to detect paddle collision with ball with right paddle
        if pongBall.getCenter().getX() > rightPaddle.getCenter().getX() - PaddleXSize / 2 and pongBall.getCenter().getY() < (rightPaddle.getCenter().getY() + PaddleYSize / 2) and pongBall.getCenter().getY() > (rightPaddle.getCenter().getY() - PaddleYSize / 2) : 
            ySpeed += .003
            xSpeed += .003
            ySpeed = -ySpeed 
            xSpeed = -xSpeed 

        #if statements to detect paddle collision with ball left paddle
        if pongBall.getCenter().getX() < leftPaddle.getCenter().getX() + PaddleXSize / 2 and pongBall.getCenter().getY() < (leftPaddle.getCenter().getY() + PaddleYSize / 2) and pongBall.getCenter().getY() > (leftPaddle.getCenter().getY() - PaddleYSize / 2) : 
            ySpeed += .003
            xSpeed += .003
            ySpeed = -ySpeed 
            xSpeed = -xSpeed 
        
        #after all conditions checked... move the ball according to modified speed
        pongBall.move(xSpeed,ySpeed)




###########################################################################################
#######         This is the first function call to start the game!!!        ###############
###########################################################################################


#Call the menu function                              
startMenu()
