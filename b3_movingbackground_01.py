#pip install pygame
#py -m pip install -U pygame --user
import pygame
pygame.init()

#Khai báo kích thước màn hình
WIDTH = 1000
HEIGHT = 500
# khai báo màu cơ bản
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Khởi tạo màn hình
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving background")
#khai báo khác
bg = pygame.image.load("images/bg.png")
#xử lý phông nền di chuyển
x_start = 0
x_stop = bg.get_width() # lấy chiều ngang của ảnh. get_height() -> chiều cao
def load_sc():
    global x_start, x_stop
    sc.blit(bg, (x_start,0))
    sc.blit(bg, (x_stop,0))
    x_start -= 2
    x_stop -= 2
    if x_stop <0:
        x_start = 0
        x_stop = bg.get_width()
#class player
class Player(pygame.sprite.Sprite):
    #trạng thái chạy
    run_images = []
    for i in range (8, 16):
        run_images.append(pygame.image.load("images/"+ str(i) +".png"))
    #trạng thái nhẩy
    jump_images = []
    for i in range (1, 8):
        jump_images.append(pygame.image.load("images/"+ str(i) +".png"))
    #trạng thái trượt
    slide_images = []
    for i in range (1, 6):
          slide_images.append(pygame.image.load("images/S"+ str(i) +".png"))
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.run_count = 0
        self.jump = False
        self.slide = False
        self.fall = False
        self.speed = 0 
        #self.surf = pygame.Surface((50, 50))
        #self.surf.fill(WHITE)
        self.image = self.run_images[self.run_count]
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    def update(self):
        if self.jump:#trạng thái nhẩy
            pass
        elif self.slide:#trạng thái trượt
            pass
        elif self.fall:#trạng thái ngã
            pass
        else:#trạng thái chạy
            self.image = self.run_images[self.run_count]
            self.run_count +=1
            if self.run_count >= len(self.run_images):
                self.run_count = 0                            

#=== Chương trình chạy====
player = Player(100, 312) #màu trắng
fps = 90# frame per second: số khung hình/s
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(fps)
    #sc.fill(WHITE)
    #sự kiện trong pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #hiển thị ảnh nền
    #sc.blit(bg, (0,0)) #ảnh, (tọa độ xuất hiện)
    load_sc()
    sc.blit(player.image, player.rect)
    player.update()
    pygame.display.update() #pygame.display.flip()
pygame.quit()
