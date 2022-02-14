import pygame
import time
import random

#import list of words from  anny words.txt file in same directory
filehandle = open('words.txt', 'r')
file=filehandle.readlines()
wordslist=[]
for word in file:
    wordslist.append(word[0:len(word)-1])

#pygame initialization
WINDOW_SIZE = WIDTH, HEIGHT = 1400,800
pygame.display.init()
global SCREEN
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.font.init()

#defining different themes
theme1=[
    (20,20,30), #background color
    (40,40,60), #backtext color
    (200,200,200) #timecolor
]
theme2=[
    (200,230,220), #background color
    (160,140,140), #backtext color
    (10,10,10) #timecolor
]
theme=theme1 #define startingtheme

#define starting values
gameduration=60
font=pygame.font.SysFont('Terminus', 80)
typedtext=''
starttime=0
starttime=time.time()
textlenght=35
correctcharacters=0
done=False
totalcorrectcharacters=0

#functions:

def createtext(length,wordslist): #function for creating a line of random words from wordlist
    text=''
    while len(text) < length:
        text+=wordslist[random.randint(0, len(wordslist)-1)]
        text+=' '
    text=text[0:len(text)-1]
    return text

def DrawWindow(): #everything that has to be done every frame except inputs


    cursortime=int((time.time()*3)%2)
    if cursortime == 0:
        cursor=''
    else:
        cursor='|'

    if starttime>0:
        timetext=str(int(timer))
    else:
        timetext=str(gameduration)


    if typedtext == text[0:len(typedtext)]:
        typedtextcolor = (100,255,70)
    else:
        typedtextcolor = (255,130,100)
    if gameduration+1-(time.time()-starttime) < 1:
        typedtextcolor = (255,255,255)

    SCREEN.fill(theme[0])
    rendertimetext=font.render(timetext,True,theme[2])
    rendertypedtext=font.render(typedtext+cursor,True,typedtextcolor)
    rendertext=font.render(text,True,theme[1])
    rendertext2=font.render(text2,True,theme[1])
    SCREEN.blit(rendertext,(100,400))
    SCREEN.blit(rendertext2,(100,480))
    SCREEN.blit(rendertypedtext,(100,400))
    SCREEN.blit(rendertimetext,(650,200))
    # testtext=font.render(str(totalcorrectcharacters),True,theme[2])
    # SCREEN.blit(testtext,(100,300))
    if done:
        wpmtext=font.render(str(int((wpm)))+' WPM',True,theme[2])
        SCREEN.blit(wpmtext,(100,100))

#create starting texts
text=createtext(textlenght,wordslist)
text2=createtext(textlenght,wordslist)
run = True

while run:

    timer = gameduration+1-(time.time()-starttime)
    if timer < 1:
        timer=0

    if int(timer) <= 1 and done==False:
        wpm=(totalcorrectcharacters/5)/(gameduration/60)
        done=True

    #calling all nessecary functions
    DrawWindow()
    pygame.display.update()

    #input calculations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            normalinput=True
            if event.key == pygame.K_F1:
                normalinput=False
                theme=theme1
            if event.key == pygame.K_F2:
                normalinput=False
                theme=theme2
            if event.key == pygame.K_F5:
                normalinput=False
                correctcharacters=0
                starttime=time.time()
                text=createtext(textlenght,wordslist)
                text2=createtext(textlenght,wordslist)
                typedtext=''
                done=False
            if (pygame.key.get_pressed()[pygame.K_LCTRL]) and event.key == pygame.K_BACKSPACE and len(typedtext)>0:
                    normalinput=False
                    if typedtext[len(typedtext)-1:] == ' ':
                        typedtext = typedtext[:-1]
                    else:
                        for i in range(20):
                            if typedtext[len(typedtext)-1:] != ' ':
                                typedtext = typedtext[:-1]
            elif event.key == pygame.K_BACKSPACE and len(typedtext)>0:
                normalinput=False
                typedtext = typedtext[:-1]
            if event.key == pygame.K_SPACE and len(text)==len(typedtext):
                for i in range(len(text)):
                    if text[i] == typedtext[i]:
                        correctcharacters+=1
                normalinput=False
                typedtext=''
                text=text2
                text2=createtext(textlenght,wordslist)
            if len(typedtext)<len(text) and normalinput:
                typedtext += event.unicode

            totalcorrectcharacters=0
            for i in range(len(typedtext)):
                if text[i] == typedtext[i]:
                    totalcorrectcharacters+=1
            totalcorrectcharacters+=correctcharacters


            
