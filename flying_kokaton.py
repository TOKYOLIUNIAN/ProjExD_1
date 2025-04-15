import os
import sys
import pygame as pg

# 设置当前目录为脚本所在目录，方便读取资源文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")  
    screen = pg.display.set_mode((800, 600))       
    clock  = pg.time.Clock()                       
    bg_img = pg.image.load("fig/pg_bg.jpg")        
    bg_img2 = pg.transform.flip(bg_img, True, False)#练习8
    kk_img = pg.image.load("fig/3.png")           
    kk_img = pg.transform.flip(kk_img, True,False) # 练习2后半
    kk_rct = kk_img.get_rect()                     # 练习10-1
    kk_rct.center = 300, 200                      # 练习10-2指定中心坐标
    tmr = 0                                        

    while True:
        for event in pg.event.get():               
            if event.type == pg.QUIT:  return             
        key_lst = pg.key.get_pressed() #练习10-3

        vx, vy = -1, 0        #演习1(#右飞)
        #print(key_lsy[pg.K_UP])
        if key_lst[pg.K_UP]:        
            vy = -1   #练习10-4
            
        if key_lst[pg.K_DOWN]:
            vy = 1   #练习10-4   

        if key_lst[pg.K_LEFT]:
            vx = -2 #练习10-4

        if key_lst[pg.K_RIGHT]:
            vx = 1 #练习10-4
       

        kk_rct.move_ip(vx, vy)
        x = tmr % 3200  #练习6
        screen.blit(bg_img, [-x, 0])     #练习6  
        screen.blit(bg_img2, [-x+1600,0])     #练习7   
        screen.blit(bg_img, [-x+3200,0])     #练习7   
        screen.blit(kk_img, kk_rct) #练习4/练习10-5   
        pg.display.update()                      
        tmr += 1                                   
        clock.tick(200)   #练习5                          

if __name__ == "__main__":
    pg.init()      
    main()         
    pg.quit()    
    sys.exit()    