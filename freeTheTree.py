### WHAT IS THIS GAME?
### Brief description of the game
# Free the Tree is a two player game where the main characters (bees) have to heal their home: a tree
# As bees, players will be able to heal the tree by shooting healing honey 
# Players must avoid the leaves, apples, and birds that the tree spits out
# If a bee dies, they can be revived by their partner 
### How interactive behaviors work
# Player movement is controlled with onKeyHold()
# Player actions are controlled with onKeyPress
# Collision is triggered using if statements, the hitsShape method, and variables
# Buttons are triggered with onMouseClick() and the hitsShape() method
# Hover is triggered with onMouseMove() and the hitsShape() method
# Finally, animation is triggered with onStep() and uses dy properties and for loops for special movement 
### Players and rule descriptions
# This is a two player game 
# Player one uses the WASD keys to move and the F key to shoot
# Player two uses the arrow keys to move and the / key to shoot
# You can revive your teammate with the spacebar as long as you are touching

#music
gameMusic =Sound('cmu://912536/36403818/15.+Tussle+Among+Trees.mp3') 
titleMusic = Sound("cmu://912536/36404411/06.+Let's+Get+Together+Now!.mp3")
startSound = Sound("cmu://912536/36404819/OOT_PressStart_Mono.wav")
buttonSound = Sound("cmu://912536/36404863/OOT_PauseMenu_Open.wav")
winMusic=Sound('cmu://912536/36405787/victoryff.swf.mp3')

#background base
app.background=gradient('deepSkyBlue','lightSkyBlue',start='top')
ground =Group( 
    Rect(-10,350,430,70,fill='green',border='black'),
    Rect(-10,365,430,50,fill=gradient('saddleBrown','sienna',start='bottom')),
    Circle(0,363,10,fill='green'),Circle(20,363,10,fill='green'),
    Circle(40,363,10,fill='green'),Circle(60,363,10,fill='green'),
    Circle(80,363,10,fill='green'),Circle(100,363,10,fill='green'),
    Circle(120,363,10,fill='green'),Circle(140,363,10,fill='green'),
    Circle(160,363,10,fill='green'),Circle(180,363,10,fill='green'),
    Circle(200,363,10,fill='green'),Circle(220,363,10,fill='green'),
    Circle(240,363,10,fill='green'),Circle(260,363,10,fill='green'),
    Circle(280,363,10,fill='green'),Circle(300,363,10,fill='green'),
    Circle(320,363,10,fill='green'),Circle(340,363,10,fill='green'),
    Circle(360,363,10,fill='green'),Circle(380,363,10,fill='green'),
    Circle(400,363,10,fill='green')
    )

###CHARACTERS AND GAME OBJECTS
#tree components
treeEyes=Label(".  .",367,240,size=25,bold=True)
treeMouth=Label('-',367,250,size=25)
tree=Group(
    Rect(350,125,40,240,fill='sienna',border='black'),
    Oval(380,100,100,50,fill='green',border='black'),
    Oval(360,150,100,50,fill='green',border='black'),
    Oval(335,115,100,50,fill='green',border='black'),
    Oval(380,130,100,50,fill='green'),
    Label('|',375,233,size=10,rotateAngle=50,bold=True),
    Label('|',359,233,size=10,rotateAngle=-50,bold=True),  
    treeEyes,
    treeMouth)
treeEvil=Group(
    Rect(363,125,40,240,fill='black',opacity=30),
    Oval(393,100,100,50,fill='black',opacity=30),
    Oval(373,150,100,50,fill='black',opacity=30),
    Oval(393,130,100,50,fill='black',opacity=30),
    Oval(348,115,100,50,fill='black',opacity=30),
    )
treeHealthBar=Rect(50,50,300,10,fill='crimson')
treeHealthBarBorder=Group(
    Rect(50,50,300,10,fill=None,border='black'),
    Label("EVIL TREE",200,30,font='montserrat',bold=True))
#player one
p1Cover= Oval(100,150,35,25,fill=None)
p1= Group(
    Label("P1",95,115),
    Oval(90,135,20,10,rotateAngle=40,fill='gainsBoro'),
    Oval(100,135,20,10,rotateAngle=-40,fill='lightGray'),
    Oval(100,150,35,25,fill='gold'),
    Circle(110,147,1),
    Line(100,138,100,162),
    Line(90,140,90,160),
    p1Cover)
p1HealthBar=Rect(30,375,100,7,fill='gold')
p1HealthBarBorder=Group(
    Rect(30,375,100,7,fill=None,border='black'),
    Label("P1",15,378,bold=True))
#player two   
p2Cover= Oval(100,250,35,25,fill=None)
p2=Group(
    Label("P2",95,215),
    Oval(90,235,20,10,rotateAngle=40,fill='gainsBoro'),
    Oval(100,235,20,10,rotateAngle=-40,fill='lightGray'),
    Oval(100,250,35,25,fill='gold'),
    Circle(110,247,1),
    Line(100,238,100,262),
    Line(90,240,90,260),
    p2Cover)
p2HealthBar=Rect(270,375,100,7,fill='gold')
p2HealthBarBorder=Group(
    Rect(270,375,100,7,fill=None,border='black'),
    Label("P2",385,378,bold=True))
    
#moving objects
clouds=Group(
    )
p1Honey=Group(
        )
p2Honey=Group(
        )
        
leaves=Group(
    )   
birds=Group(
    ) 

def drawApple (xCenter,yCenter):
    apple = Group(
        Circle(xCenter,yCenter,8,fill='crimson'),
        Line(xCenter,yCenter-4,xCenter,yCenter-9))
    return apple
apple1=drawApple(325,105)
apple2=drawApple(380,130)
apple1.dy=3
apple2.dy=3

#character properties
p1.health=3000
p2.health=3000
p1.canMove=False
p2.canMove=False

###MENU SCREEN COMPONENTS
#text
title=Group(
    Label("Free The Tree!",197,200,size=40,font='montserrat',bold=True),
    Label("Free The Tree!",203,200,size=40,font='montserrat',bold=True),
    Label("Free The Tree!",200,203,size=40,font='montserrat',bold=True),
    Label("Free The Tree!",200,197,size=40,font='montserrat',bold=True),
    Label("Free The Tree!",200,200,size=40,font='montserrat',bold=True,fill='gold')
    )
controls= Group(
    Label("Controls",200,70,size=40,font='montserrat',),
    Label("p1 uses keys WASD",180,130,font='montserrat',),
    Label("for movement and uses",180,150,font='montserrat',),
    Label("the F key to shoot honey",180,170,font='montserrat',),
    Label("P1",45,115),
    Oval(40,135,20,10,rotateAngle=40,fill='gainsBoro'),
    Oval(50,135,20,10,rotateAngle=-40,fill='lightGray'),
    Oval(50,150,35,25,fill='gold'),
    Circle(60,147,1),
    Line(50,138,50,162),
    Line(40,140,40,160),
    Rect(280,150,20,20,fill='gold'),
    Label('A',290,160,font='montserrat'),
    Rect(310,150,20,20,fill='gold'),
    Label('S',320,160,font='montserrat'),
    Rect(340,150,20,20,fill='gold'),
    Label('D',350,160,font='montserrat'),
    Rect(310,120,20,20,fill='gold'),
    Label('W',320,130,font='montserrat'),
    Label("p2 uses the arrow keys",220,220,font='montserrat'),
    Label("for movement and uses",220,240,font='montserrat'),
    Label("the / key to shoot honey",220,260,font='montserrat'),
    Label("P2",335,210),
    Oval(330,225,20,10,rotateAngle=40,fill='gainsBoro'),
    Oval(340,225,20,10,rotateAngle=-40,fill='lightGray'),
    Oval(340,240,35,25,fill='gold'),
    Circle(350,237,1),
    Line(340,228,340,252),
    Line(330,250,330,230),
    Rect(40,240,20,20,fill='gold'),
    Label('<',50,250,font='montserrat'),
    Rect(70,240,20,20,fill='gold'),
    Label('v',80,250,font='montserrat'),
    Rect(100,240,20,20,fill='gold'),
    Label('>',110,250,font='montserrat'),
    Rect(70,210,20,20,fill='gold'),
    Label('^',80,220,font='montserrat'),
    Label("Both players can use the space key to revive eachother",200,290,font='montserrat'),
    Label("as long as they are touching",200,310,font='montserrat'))
    
#dialogue 
dialogueBox=Group(
    Circle(100,350,22,fill='black'),
    Circle(300,350,22,fill='black'),
    Rect(200,350,204,44,align='center',fill='black'),
    Circle(200,380,17,fill='black'),
    Circle(300,380,17,fill='black'),
    Rect(250,380,104,34,align='center',fill='black'),
    Circle(100,350,20,fill='gold'),
    Circle(300,350,20,fill='gold'),
    Rect(200,350,200,40,align='center',fill='gold'),
    Circle(200,380,15,fill='yellow'),
    Circle(300,380,15,fill='yellow'),
    Rect(250,380,100,30,align='center',fill='yellow'),
    )
dialogue= Label("",200,350,font='montserrat')
skipInstructions=Label("",250,380,font='montserrat')

#end screens
restartScreen= Group(
    Rect(0,0,400,400,fill='lightSkyBlue'),
    Rect(180,70,40,150,fill='sienna'),
    Oval(205,90,100,50,fill='green'),
    Oval(190,100,100,50,fill='green'),
    Oval(210,110,100,50,fill='green'),
    Oval(200,115,100,50,fill='green'),
    Label('.',190,165,size=40),
    Label('.',210,165,size=40),
    Label('-',200,170,size=20),
    Label('|',210,155,size=10,rotateAngle=50,bold=True),
    Label('|',190,155,size=10,rotateAngle=-50,bold=True),  
    Label("Game Over",200,250,size=30,font='montserrat'),
    Rect(0,0,400,400,opacity=20))
winScreen= Group(
    Rect(0,0,400,400,fill='lightSkyBlue'),
    Rect(180,70,40,150,fill='sienna'),
    Oval(205,90,100,50,fill='green'),
    Oval(190,100,100,50,fill='green'),
    Oval(210,110,100,50,fill='green'),
    Oval(200,115,100,50,fill='green'),
    Label('.',190,165,size=30),
    Label('.',210,165,size=30),
    Label('D',200,173,size=15,rotateAngle=90),
    Label("The Tree Is Free!!",200,250,size=30,font='montserrat'))
    
#buttons and button outlines
startButtonHover=Group(
    Circle(150,300,22,fill='black'),
    Circle(250,300,22,fill='black'),
    Rect(200,300,104,44,align='center',fill='black'),)
startButton=Group(
    Circle(150,300,20,fill='gold'),
    Circle(250,300,20,fill='gold'),
    Rect(200,300,100,40,align='center',fill='gold'),
    Label("START",200,300,font='montserrat'))
   
controlsButtonHover=Group(
    Circle(150,350,22,fill='black'),
    Circle(250,350,22,fill='black'),
    Rect(200,350,104,44,align='center',fill='black'))    
controlsButton=Group(
    Circle(150,350,20,fill='gold'),
    Circle(250,350,20,fill='gold'),
    Rect(200,350,100,40,align='center',fill='gold'),
    Label("CONTROLS",200,350,font='montserrat'))
    
gotItButtonHover=Group(
    Circle(150,350,22,fill='black'),
    Circle(250,350,22,fill='black'),
    Rect(200,350,104,44,align='center',fill='black'),)  
gotItButton=Group(
    Circle(150,350,20,fill='gold'),
    Circle(250,350,20,fill='gold'),
    Rect(200,350,100,40,align='center',fill='gold'),
    Label("GOT IT",200,350,font='montserrat'))

restartButtonHover=Group(
    Circle(150,300,22,fill='black'),
    Circle(250,300,22,fill='black'),
    Rect(200,300,104,44,align='center',fill='black'),)
restartButton=Group(
    Circle(150,300,20,fill='gold'),
    Circle(250,300,20,fill='gold'),
    Rect(200,300,100,40,align='center',fill='gold'),
    Label("RETRY",200,300,font='montserrat'))

playAgainButtonHover=Group(
    Circle(150,300,22,fill='black'),
    Circle(250,300,22,fill='black'),
    Rect(200,300,104,44,align='center',fill='black'),)   
playAgainButton=Group(
    Circle(150,300,20,fill='gold'),
    Circle(250,300,20,fill='gold'),
    Rect(200,300,100,40,align='center',fill='gold'),
    Label("PLAY AGAIN",200,300,font='montserrat'))



###FUNCTIONALITY 
#app properties
app.phase=0
app.flashCounter=1
app.leafResetCounter=0
app.playerDamage=1.5
###HELPER FUNCTIONS 
def initialize():
    app.stepsPerSecond=20
    titleMusic.play()
    #moves objects off/on screen
    startButton.centerX=200
    controlsButton.centerX=200
    gotItButton.centerX=1000
    restartButton.centerX=1000
    playAgainButton.centerX=1000
    tree.centerX=1000
    p1Honey.clear()
    p2Honey.clear()
    p1.centerX=100
    p1.centerY=150
    p1.rotateAngle=0
    p2.centerX=100
    p2.centerY=250
    p2.rotateAngle=0
    apple1.centerX=325
    apple1.centerY=105
    apple2.centerX=380
    apple2.centerY=130
    #hides/shows objects
    title.visible=True
    controls.visible=False
    p1.visible=False
    p2.visible=False
    p1.canMove=False
    p2.canMove=False
    restartScreen.visible=False
    dialogueBox.visible=False
    treeHealthBar.visible=False
    treeHealthBarBorder.visible=False
    p1HealthBar.visible=False
    p1HealthBarBorder.visible=False
    p2HealthBar.visible=False
    p2HealthBarBorder.visible=False
    winScreen.visible=False
    startButtonHover.visible=False
    controlsButtonHover.visible=False
    restartButtonHover.visible=False
    gotItButtonHover.visible=False
    playAgainButtonHover.visible=False
    leaves.visible=False
    birds.visible=False
    apple1.visible=False
    apple2.visible=False
    treeEvil.visible=False
    #reset values
    p1.health=3000
    p2.health=3000
    treeMouth.value='-'
    treeEvil.opacity=50
    treeHealthBar.width=300
    leaves.dy=3
    app.playerDamage=1.5
    app.phase=0
initialize()

#drawing clouds
def drawCloud(x, y):
    cloud=Group(
        Oval(x, y, 100, 45, fill='white',opacity=90),
        Circle(x + 40, y - 10, 20, fill='white',opacity=90),
        Circle(x + 10, y - 20, 30, fill='white',opacity=90),
        Circle(x - 15, y - 20, 30, fill='white',opacity=90),
        Circle(x - 30, y, 20, fill='white',opacity=90))
    return cloud
clouds.add(drawCloud(400,200))
clouds.add(drawCloud(550,300))
clouds.add(drawCloud(640,130))

#drawing leaves
def drawLeaf (xCenter,yCenter,angle):
    leaf = Group(
        Oval(xCenter,yCenter,13,15,fill='green'),
        Polygon(xCenter-5,yCenter-5,xCenter+5,yCenter-5,xCenter,yCenter-15,fill='green'),
        Line(xCenter,yCenter,xCenter,yCenter+14,fill='darkGreen'))
    leaf.rotateAngle=angle
    return leaf
leaves.add(drawLeaf(50,0,40))
leaves.add(drawLeaf(150,-30,20))
leaves.add(drawLeaf(250,0,-40))

leaves.add(drawLeaf(100,-150,-40))
leaves.add(drawLeaf(200,-170,20))

leaves.add(drawLeaf(20,-350,-40))
leaves.add(drawLeaf(340,-270,20))
leaves.dy=3
#drawing birds
def drawBird (xCenter,yCenter):
    bird = Group(
        Oval(xCenter,yCenter+3,20,15,fill='blue',rotateAngle=30),
        Oval(xCenter,yCenter,25,8,fill='blue',rotateAngle=-30),
        Circle(xCenter-10,yCenter,7,fill='blue'),
        Circle(xCenter-10,yCenter-2,1),
        Polygon(xCenter-16,yCenter-2,xCenter-16,yCenter+2,xCenter-23,yCenter,fill='gold'),
        Polygon(xCenter+18,yCenter+12,xCenter+8,yCenter+10,xCenter+8,yCenter,fill='blue'))
    return bird
birds.add(drawBird(380,255))
birds.add(drawBird(580,255))

#toggle functions
def toggleStartScreen():
    if(title.visible==True):
        startButton.centerX=1000
        controlsButton.centerX=1000
        title.visible=False
    else:
        startButton.centerX=200
        controlsButton.centerX=200
        title.visible=True

def toggleControlsScreen():
    if(controls.visible==True):
        controls.visible=False
        gotItButton.centerX=1000
        gotItButtonHover.visible=False
    else:
        controls.visible=True
        gotItButton.centerX=200
        
def toggleGameScreen():
    if(tree.centerX==370):
        tree.centerX==1000
        apple1.visible=False
        apple2.visible=False
        p1.visible=False
        p2.visible=False
    else:
        apple1.visible=True
        apple2.visible=True
        tree.centerX=370
        treeEvil.visible=True
        p1.visible=True
        p2.visible=True
        dialogueBox.visible=True
        dialogue.value='Oh no! Our tree has been possessed!'
        skipInstructions.value='next [space]'
        
def toggleRestartScreen():
        restartScreen.visible=True
        restartButton.centerX=200
        gameMusic.pause()

def toggleWinScreen():
        winScreen.visible=True
        playAgainButton.centerX=200
        gameMusic.pause()
        winMusic.play()

###EVENT FUNCTIONS 
#When the mouse is clicked
def onMousePress(mouseX,mouseY):
    #if the control button is clicked
    if(controlsButton.hits(mouseX,mouseY)):
        toggleStartScreen()
        toggleControlsScreen()
        buttonSound.play()
    
    #if the start button is clicked
    elif(startButton.hits(mouseX,mouseY)):
        toggleStartScreen()
        toggleGameScreen()
        startButtonHover.visible=False
        controlsButtonHover.visible=False
        startSound.play()
        
    #if the got it button is clicked
    elif(gotItButton.hits(mouseX,mouseY)):
        toggleControlsScreen()
        toggleStartScreen()
        buttonSound.play()
    
    #if the restart button is clicked
    elif(restartButton.hits(mouseX,mouseY)):
        initialize()
        leaves.centerY=-175
        birds.clear()
        birds.add(drawBird(380,255))
        birds.add(drawBird(580,255))
        buttonSound.play()
    
    #if the play again button is clicked
    elif(playAgainButton.hits(mouseX,mouseY)):
        initialize()
        leaves.centerY=-175
        birds.clear()
        birds.add(drawBird(380,255))
        birds.add(drawBird(580,255))
        buttonSound.play()
        
#when the mouse moves
def onMouseMove(mouseX,mouseY):
    #if the control button is hovered over
    if(controlsButton.hits(mouseX,mouseY)):
            controlsButtonHover.visible=True
    else:
        controlsButtonHover.visible=False

    #if the start button is hovered over
    if(startButton.hits(mouseX,mouseY)):
        startButtonHover.visible=True
    else:
        startButtonHover.visible=False

    #if the restart button is hovered over    
    if(restartButton.hits(mouseX,mouseY)):
        restartButtonHover.visible=True
    else:
        restartButtonHover.visible=False

    #if the got it button is hovered over   
    if(gotItButton.hits(mouseX,mouseY)):
        gotItButtonHover.visible=True
    else:
        gotItButtonHover.visible=False

    #if the play again button is hovered over
    if(playAgainButton.hits(mouseX,mouseY)):
        playAgainButtonHover.visible=True
    else:
        playAgainButtonHover.visible=False
    
#when keys are held down
def onKeyHold(keys):
    #p1 movement
    if(p1.canMove==True):
        if('w' in keys):
            p1.centerY-=4
        if('a' in keys):
            p1.centerX-=4
        if('s' in keys):
            p1.centerY+=4
        if('d' in keys):
            p1.centerX+=4
        
    #p2 movement
    if(p2.canMove==True):
        if('up' in keys):
            p2.centerY-=4
        if('left' in keys):
            p2.centerX-=4
        if('down' in keys):
            p2.centerY+=4
        if('right' in keys):
            p2.centerX+=4

#when a key is pressed
def onKeyPress(key):
    #if space bar is pressed
    if(key=='space'):
        #skipping through dialogue 
        if(dialogue.value=="Oh no! Our tree has been possessed!"):
            dialogue.value="Shoot your healing honey at the tree"
        elif(dialogue.value=="Shoot your healing honey at the tree"):
            dialogue.value="Avoid the leaves, birds, and apples"
        elif(dialogue.value=="Avoid the leaves, birds, and apples"):
            dialogue.value="Please, brave heroes! Save the tree!"
        elif(dialogue.value=="Please, brave heroes! Save the tree!"):
            #starting the game 
            titleMusic.pause()
            gameMusic.play(loop=True)
            dialogueBox.visible=False
            dialogue.value=""
            skipInstructions.value=""
            p1.canMove=True
            p2.canMove=True
            app.phase=1
            treeHealthBar.visible=True
            treeHealthBarBorder.visible=True
            p1HealthBar.visible=True
            p1HealthBarBorder.visible=True
            p2HealthBar.visible=True
            p2HealthBarBorder.visible=True
        #checking for reviving 
        if(p1.hitsShape(p2)):
            if (p1.canMove==False):
                p1.canMove=True
                p1.rotateAngle=0
                p1.health=1000
            if (p2.canMove == False):
                p2.canMove=True
                p2.rotateAngle=0
                p2.health=1000
    
    #shooting honey  
    if(p1.canMove==True):
        if key == 'f':
            p1Honey.add (Oval(p1.right,p1.centerY,10,5,fill=gradient('orange','gold')))
    if(p2.canMove==True):
       if key == '/':
            p2Honey.add (Oval(p2.right,p2.centerY,10,5,fill=gradient('orange','gold')))
            
#called continuosly
def onStep():
    #resetting bee covers so they can't be locked as visible  
    p1Cover.fill=None
    p2Cover.fill=None
    
    #removing honey projectiles so they don't go through the tree 
    for honey in p1Honey:
        if (honey.hitsShape(tree)):
            p1Honey.remove(honey)
    for honey in p2Honey:
        if (honey.hitsShape(tree)):
            p2Honey.remove(honey)
    
    #making a counter to count every other step 
    #(this will help me make the bees flash when they get hit)
    if(app.flashCounter==1):
        app.flashCounter=2
    elif(app.flashCounter==2):
        app.flashCounter=1
        
    #moving honey to the right 
    if (app.phase>0 and restartButton.centerX>400):
        p1Honey.centerX+=5
        p2Honey.centerX+=5
        
    #checking for collision with player 
    if (p1.hitsShape(tree)):
        p1.health-=100
        if(app.flashCounter==1 and p1.canMove==True):
            p1Cover.fill='white'
    if (p2.hitsShape(tree)):
        p2.health-=100
        if(app.flashCounter==1 and p2.canMove==True):
            p2Cover.fill='white'
    if (p1.hitsShape(leaves) or p1.hitsShape(birds)or p1.hitsShape(apple1) or p1.hitsShape(apple2)or p1.hitsShape(ground)):
        p1.health-=100
        if(app.flashCounter==1 and p1.canMove==True):
            p1Cover.fill='white'
    if (p2.hitsShape(leaves) or p2.hitsShape(birds) or p2.hitsShape(apple1) or p2.hitsShape(apple2)or p2.hitsShape(ground)):
        p2.health-=100
        if(app.flashCounter==1 and p2.canMove==True):
            p2Cover.fill='white'    
    
    #changing phases based on the tree health
    if(treeHealthBar.width<=200 and treeHealthBar.width>100):
        app.phase=2
    if(treeHealthBar.width<=100):
        app.phase=3   

    #controlling tree health and checking for game win 
    
    #stops movement and toggles win screen
    if(treeHealthBar.width<=3 and winScreen.visible==False):
        app.stepsPerSecond=0
        toggleWinScreen()
        treeHealthBar.visible=False
        p1.canMove=False
        p2.canMove=False
        app.phase=0
    #if the players haven't won, decrease the tree's health
    elif (p1Honey.hitsShape(tree) or p2Honey.hitsShape(tree)):
        treeHealthBar.width-= app.playerDamage
        treeEvil.opacity=treeHealthBar.width/6
        
    #stopping movement for dead players
    if(p1.health<=0):
        p1.canMove=False
        p1.rotateAngle=180
        p1HealthBar.width=1
    else:
        p1HealthBar.width=p1.health/30
    if(p2.health<=0):
        p2.canMove=False
        p2.rotateAngle=180
        p2HealthBar.width=1
    else:
        p2HealthBar.width=p2.health/30
    
    #triggering game over
    if(p2.health<=0 and p1.health<=0):
        toggleRestartScreen()
        
    ###PHASES (increasing difficulty)
    else:
        #phase 1 with only leaves
        if (app.phase>0):
            leaves.visible=True
            for leaf in leaves:
                leaf.centerY+=leaves.dy
                if (leaf.centerY>350):
                    leaf.centerY=0
                        
        #phase 2 birds added and leaves speed up
        if (app.phase>1):
            leaves.dy=4
            birds.visible=True
            treeMouth.value='O'
            for bird in birds:
                bird.centerX -= 3
                if (bird.right<0):
                    bird.centerX=350
        #phase 3 apples added, leaves speed up, damage is decreased
        if (app.phase>2):
            app.playerDamage=0.5
            leaves.dy=5
            apple1.centerX-=4
            if (apple1.centerY>=350):
                apple1.dy=-6
            elif (apple1.centerY<=150):
                apple1.dy=6
            if(apple1.right<0):
                apple1.centerX=380
            apple1.centerY+=apple1.dy
            apple2.centerX-=4
            if (apple2.centerY>=350):
                apple2.dy=-6
            elif (apple2.centerY<=170):
                apple2.dy=6
            if(apple2.right<0):
                apple2.centerX=380
            apple2.centerY+=apple2.dy

#moving clouds
    for cloud in clouds:
        cloud.centerX-=3
        if (cloud.right<0):
            cloud.centerX=480
    clouds.toBack()

#prevents players from going off screen
    if(p1.left<0):
        p1.left=0
    if(p1.centerY<20):
        p1.centerY=20
    if(p1.right>400):
        p1.right=400
    if(p1.centerY>350):
        p1.centerY=350
