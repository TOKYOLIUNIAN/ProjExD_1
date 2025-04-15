import os
import sys
import pygame as pg

# 设置当前目录为脚本所在目录，方便读取资源文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")  # 设置窗口标题
    screen = pg.display.set_mode((800, 600))       # 创建窗口，大小800x600
    clock  = pg.time.Clock()                       # 设置时钟
    bg_img = pg.image.load("fig/pg_bg.jpg")        # 加载背景图像
    bg_img2 = pg.transform.flip(bg_img, True, False)#练习8
    kk_img = pg.image.load("fig/3.png")           # 加载角色图像
    kk_img = pg.transform.flip(kk_img, True,False) # 练习2后半
    tmr = 0                                         # 计时器初始化

    while True:
        for event in pg.event.get():               # 处理事件
            if event.type == pg.QUIT:  return             # 如果点击关闭窗口
                                            # 退出主循环
        x = tmr
        screen.blit(bg_img, [-x, 0])     #练习6  
        screen.blit(bg_img, [-x+1600,0])     #练习7    # 绘制背景图像
        screen.blit(kk_img, [300, 200])  #练习4   
        pg.display.update()                        # 更新显示内容
        tmr += 1                                   
        clock.tick(200)   #练习5                          # 控制帧率（每秒10帧）

if __name__ == "__main__":
    pg.init()      # 初始化 pygame 模块
    main()         # 执行主函数
    pg.quit()      # 关闭 pygame 模块
    sys.exit()     # 退出程序
