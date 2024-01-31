import pygame
import random
import time
# 初始化游戏
pygame.init()

# 定义屏幕尺寸
screen_width = 640
screen_height = 480
gamefps=144
#定义蛇的尺寸和速度
snake_size = 20
speed_up=False#是否加速
#导入资源
background=pygame.image.load("resource/oipc.jpg")
sound=pygame.mixer.Sound("resource/The sound of a bite of apple.wav")
keystrokeSound=pygame.mixer.Sound("resource/Game Keystroke Sound.wav")
vicsound=pygame.mixer.Sound("resource/Upgrade _ Victory _ Pass sound effects.wav")
explode_sound=pygame.mixer.Sound("resource/Explodeound.ogg")
head=pygame.image.load("resource/head.png")
body=pygame.image.load("resource/body.png")
apple=pygame.image.load("resource/apple.png")
tail=pygame.image.load("resource/tail.png")
mushroom=pygame.image.load("resource/mushroom.png")
gameCover=pygame.image.load("resource/gameCover.jpg")
gameOver=pygame.image.load("resource/gameOver.png")
victory=pygame.image.load("resource/victory.jpg")
tnt=pygame.image.load("resource/TNT.png")
explode=pygame.image.load("resource/explode.png")
game_over_sound=pygame.mixer.Sound("resource/Game Failed Funny Sound Effects_耳聆网.wav")
eat_mushroom_sound=pygame.mixer.Sound("resource/Steve's Injury Sound Effect_耳聆网.ogg")
#调整图片资源尺寸
background=pygame.transform.scale(background,(screen_width,screen_height))
gameCover=pygame.transform.scale(gameCover,(screen_width,screen_height+15))
gameOver=pygame.transform.scale(gameOver,(screen_width,screen_height+15))
victory=pygame.transform.scale(victory,(screen_width,screen_height+15))
body=pygame.transform.scale(body,(snake_size,snake_size))
apple=pygame.transform.scale(apple,(snake_size,snake_size))
head=pygame.transform.scale(head,(snake_size,snake_size))
tail=pygame.transform.scale(tail,(snake_size,snake_size))
mushroom=pygame.transform.scale(mushroom,(snake_size,snake_size))
tnt=pygame.transform.scale(tnt,(snake_size,snake_size))
explode=pygame.transform.scale(explode,(snake_size+100,snake_size+100))
#调整不透明度
victory.set_alpha(200)
#获得不同角度的蛇身
head_left=head
head_down=pygame.transform.rotate(head,90)
head_up=pygame.transform.rotate(head,-90)
head_right=pygame.transform.rotate(head,180)

tail_left=tail
tail_down=pygame.transform.rotate(tail,90)
tail_up=pygame.transform.rotate(tail,-90)
tail_right=pygame.transform.rotate(tail,180)

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height+15))#hight加15是为了给状态栏留空间
pygame.display.set_caption('贪吃蛇小游戏')

#播放游戏音乐
pygame.mixer.music.load("resource/NewPiano.mp3")
pygame.mixer.music.play(-1)
#________________________________________________________开始界面__________________________________________________
# 创建字体对象
font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 36)

# 创建开始提示文本
start_text = font.render("按空格键继续", True, (255, 255, 255))

# 控制游戏结束的变量
game_over = True
# 窗口循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over=False
                keystrokeSound.play()
                break
    if(not game_over):
        break            

    # 绘制背景
    screen.blit(gameCover,gameCover.get_rect())
    
    # 绘制开始提示文本
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 280))

    # 刷新窗口
    pygame.display.update()
#_______________________________________________________玩法说明_________________________________________________
# 创建字体对象
font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 15)
game_over=True
# 创建提示文本
text1 = font.render("玩法说明", True, (0, 0, 0))
text2 = font.render("使用四个方向键操作", True, (0, 0, 0))
text3 = font.render("吃一个苹果加10分,200分通关", True, (0, 0, 0))
text4 = font.render("按下空格键可以让蛇蛇加速,松开恢复原速度", True, (0, 0, 0))
text5 = font.render("吃下蘑菇会进入眩晕状态,方向键对调,左变右,上变下,同时吃p苹果得分翻倍", True, (0, 0, 0))
text6 = font.render("每隔一段时间就会落下炸弹,要及时躲避,按下空格键可以加速炸弹落下", True, (0, 0, 0))
#窗口循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over=False
                keystrokeSound.play()
                break
    if(not game_over):
        break            

    # 绘制背景
    screen.blit(gameCover,gameCover.get_rect())
    
    # 绘制开始提示文本
    screen.blit(text1, (screen.get_width() // 2 - text1.get_width() // 2, 50))
    screen.blit(text2, (screen.get_width() // 2 - text2.get_width() // 2, 80))
    screen.blit(text3, (screen.get_width() // 2 - text3.get_width() // 2, 110))
    screen.blit(text4, (screen.get_width() // 2 - text4.get_width() // 2, 290))
    screen.blit(text5, (screen.get_width() // 2 - text5.get_width() // 2, 320))
    screen.blit(text6, (screen.get_width() // 2 - text6.get_width() // 2, 350))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 380))

    # 刷新窗口
    pygame.display.update()
    
#___________________________________________________游戏主体____________________________________________________    
# 创建字体对象
font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 15)
# 创建状态栏Surface对象
status_bar = pygame.Surface((screen.get_width(), 15))
# 设置状态栏背景颜色
status_bar.fill((255, 255, 0))

# 在状态栏上绘制文本
status="正常"
score=0#当游戏得分达到200则游戏胜利
fulscore=200
text = font.render("状态：{0}  得分：{1}".format(status,score), True, (0, 0, 0))
status_bar.blit(text, (10, 2))
# 渲染状态栏
screen.blit(status_bar, (0, screen.get_height() - status_bar.get_height()))

def reset_statusbar():
    # 重新渲染状态栏上的文本
    text = font.render("状态：{0}  得分：{1}".format(status,score), True, (0, 0, 0))
    status_bar.fill((255, 255, 0))
    status_bar.blit(text, (10, 2))
    screen.blit(status_bar, (0, screen.get_height() - status_bar.get_height()))
    
# 蛇的初始位置和方向
snake_head = [screen_width // 2, screen_height // 2]
snake_body = [[screen_width // 2, screen_height // 2], [screen_width // 2 - 20, screen_height // 2],
              [screen_width // 2 - 40, screen_height // 2]]
direction = 'RIGHT'
tail=tail_right

 
#道具刷新
class Object:
    def __init__(self,image):
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, (screen_width // snake_size)) * snake_size
        self.rect.y = random.randrange(1, (screen_height // snake_size)) * snake_size
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def reset(self):
        self.rect.x = random.randrange(1, (screen_width // snake_size)) * snake_size
        self.rect.y = random.randrange(1, (screen_height // snake_size)) * snake_size

#苹果
class Apple(Object):
    def __init__(self, image):
        super().__init__(image)

#创建一个苹果对象
apple_1=Apple(apple)
                
#毒蘑菇

class Mushroom(Object):
    def __init__(self, image):
        super().__init__(image)
#创建一个蘑菇对象
mushroom_1=Mushroom(mushroom)
    
mushroomEvent=pygame.USEREVENT+1
pygame.time.set_timer(mushroomEvent,10000)#每10秒刷新一个毒蘑菇
mflag=False#毒蘑菇是否存在
dizziness=False#蛇是否处于眩晕状态,如果蛇处于眩晕，则移动方向与控制相反

#tnt
class TNT(Object):
    def __init__(self,image):
        super().__init__(image)
        self.rect.y = snake_size
        self.velocity =0 # 初始速度
        self.acceleration = snake_size*0.20  # 加速度，表示重力

    def reset(self):
        self.rect.x = random.randrange(1, (screen_width // snake_size)) * snake_size
        self.rect.y = snake_size
        self.velocity =0 # 初始速度
        self.acceleration = snake_size*0.20  # 加速度，表示重力
#创建一个tnt对象
tnt_1=TNT(tnt)  

tntEvent=pygame.USEREVENT+2
pygame.time.set_timer(tntEvent,5000)#每5秒刷新一个炸弹
tflag=False#炸弹是否存在

clock = pygame.time.Clock()

# 定义对象的帧数
snake_fps = 10
multi_fps=2
tnt_fps = 10

# 定义对象的更新时间间隔
snake_update_interval = 1000 // snake_fps
tnt_update_interval = 1000 // tnt_fps

# 定义对象的计时器
snake_timer = pygame.time.get_ticks()
tnt_timer = pygame.time.get_ticks()
      
# 游戏循环
while not game_over: 
    # 绘制背景
    screen.blit(background,background.get_rect())   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if not dizziness: 
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key==pygame.K_SPACE and (not speed_up):
                    snake_fps*=multi_fps
                    snake_update_interval = 1000 // snake_fps
                    speed_up=not speed_up
                status="正常"
            else:
                if event.key == pygame.K_UP and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_DOWN and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_LEFT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_RIGHT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key==pygame.K_SPACE and (not speed_up):
                    snake_fps*=multi_fps
                    snake_update_interval = 1000 // snake_fps
                    speed_up=not speed_up
                status="眩晕"
                
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE and speed_up:
                    snake_fps/=multi_fps
                    snake_update_interval = 1000 // snake_fps
                    speed_up=not speed_up
                #蘑菇刷新
        elif event.type==mushroomEvent:
            mflag=not mflag
            mushroom_1.reset()
                #tnt刷新
        elif event.type==tntEvent:
            tflag=not tflag
            #重置tnt数据
            tnt_1.reset()
    
    # 更新蛇的位置
    current_time = pygame.time.get_ticks() 
        # 移动蛇的身体部分
    if current_time - snake_timer >= snake_update_interval:
        if direction == 'UP':
            snake_head[1] -= snake_size
            head=head_up 
        elif direction == 'DOWN':
            snake_head[1] += snake_size
            head=head_down
        elif direction == 'LEFT':
            snake_head[0] -= snake_size
            head=head_left
        elif direction == 'RIGHT':
            snake_head[0] += snake_size
            head=head_right            
        #获取尾巴的方向以控制蛇尾的旋转
        
        x=snake_body[-2][0]-snake_body[-3][0]
        y=snake_body[-2][1]-snake_body[-3][1]
        if x>0:x=1
        elif x<0:x=-1
        if y>0:y=1
        elif y<0:y=-1
        d1=complex(x,y)#倒数第二节指向倒数第三节的方向
        x=snake_body[-1][0]-snake_body[-2][0]
        y=snake_body[-1][1]-snake_body[-2][1]
        if x>0:x=1
        elif x<0:x=-1
        if y>0:y=1
        elif y<0:y=-1
        d2=complex(x,y)#最后一节指向倒数第二节的方向
        #在拐角处要进行变换，保证蛇尾转动流畅
        if ((d1.real-d2.real==0)and(d1.imag-d2.imag!=0))or((d1.real-d2.real!=0)and(d1.imag-d2.imag==0)):
            if d2.real==0 and d2.imag>0:
                tail=tail_up
            elif d2.real==0 and d2.imag<0:
                tail=tail_down
            elif d2.real>0 and d2.imag==0:
                tail=tail_left
            else: tail=tail_right
            
        else:    
            if d1.real==0 and d1.imag>0:
                tail=tail_up
            elif d1.real==0 and d1.imag<0:
                tail=tail_down
            elif d1.real>0 and d1.imag==0:
                tail=tail_left
            else: tail=tail_right
        
        # 判断蛇是否吃到食物
        if snake_head[0] == apple_1.rect.x and snake_head[1] == apple_1.rect.y:
            apple_1.reset()            
            if not dizziness:
                score+=10
            else: score+=20
            sound.play()
        else:
            snake_body.pop()
        # 增加蛇的长度
        snake_body.insert(0, list(snake_head))
        
        #判断蛇是否吃到毒蘑菇
        if snake_head[0] ==mushroom_1.rect.x and snake_head[1] == mushroom_1.rect.y:
            dizziness=not dizziness
            mflag=not mflag
            mushroom_1.reset()
            reset_statusbar()
            eat_mushroom_sound.play()     
                     
        snake_timer = current_time

      # 更新TNT的位置
    if current_time - tnt_timer >= tnt_update_interval:
        if tflag:    
            tnt_1.velocity += tnt_1.acceleration
            tnt_1.rect.y += tnt_1.velocity
            
            tnt_timer = current_time
    
    
    #绘制蛇头
    screen.blit(head,pygame.Rect(snake_body[0][0], snake_body[0][1], snake_size, snake_size)) 
    #绘制蛇身
    for position in snake_body[1:-1]:
            screen.blit(body,pygame.Rect(position[0], position[1], snake_size, snake_size))
    #绘制蛇尾
    screen.blit(tail,pygame.Rect(snake_body[-1][0], snake_body[-1][1], snake_size, snake_size))
    
    # 绘制苹果
    apple_1.draw(screen)
    #绘制蘑菇
    if mflag:
        mushroom_1.draw(screen)
    #绘制tnt
    if tflag:    
        tnt_1.draw(screen)
    
              
    # 判断蛇是否碰到边界或自己的身体
    if snake_head[0] < 0 or snake_head[0] >= screen_width or snake_head[1] < 0 or snake_head[1] >= screen_height \
            or snake_head in snake_body[2:]:
        game_over = True
        game_over_sound.play()
        screen.blit(gameOver,gameOver.get_rect())
    elif score>=fulscore:#得满分则结束游戏
        game_over=True
        vicsound.play()
        screen.blit(victory,victory.get_rect())
        
    #判断蛇是否被炸
    if tflag:
        for item in snake_body:
            if (abs(item[0]-tnt_1.rect.x)<snake_size)\
                and (abs(item[1]-tnt_1.rect.y)<snake_size):
                game_over = True
                tflag=False
                explode_sound.play()
                game_over_sound.play()
                screen.blit(explode,(tnt_1.rect.x-50,tnt_1.rect.y-50),explode.get_rect())
                screen.blit(gameOver,gameOver.get_rect())
                break
                
    # 重新渲染状态栏上的文本
    reset_statusbar()
    
    # 更新屏幕
    pygame.display.update()
    #控制游戏时钟的变量
    clock.tick(gamefps)
  
    if(game_over):
        pygame.mixer.music.stop()
        time.sleep(5)
    
# 退出游戏
pygame.quit()
