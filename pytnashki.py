# coding: utf8

# импортируем библиотеку пигуейм и модуль рандома

import pygame
import random

# определяем размеры игрового поля и шрифта, который будет использоваться в игре, 
# сколько будет ячеек в одной колонке/столбце, какого они будут размера,
# сколько их будет всего

SCREEN_X = 300
SCREEN_Y = SCREEN_X

BLOCKS_IN_LINE = 4
BLOCK_SIZE = SCREEN_X // BLOCKS_IN_LINE

GAME = BLOCKS_IN_LINE*BLOCKS_IN_LINE - 1

# задаем цвет фона и цифры

#BACKGROUND = 'fon.png'
BACKGROUND_COLOR = (255, 255, 255)
DIGIT_COLOR = (0, 0, 0)

# сколько раз будем тасовать поле, значение увеличить по мере увеличения BLOCKS_IN_LINE

RANDOM = 10**(BLOCKS_IN_LINE-1)

# инициализируем шрифты

pygame.font.init()
DIGIT_SIZE = BLOCK_SIZE//2
FONT = pygame.font.SysFont("comicsansms", DIGIT_SIZE)

# класс блока, имеет размер, цвет числа, число и положение

class Block:
    def __init__(self, color, digit, x, y):
        self.digit = digit
        self.color = color
        self.x = x
        self.y = y

    def render(self, where):
        self.number = FONT.render('  ' + str(self.digit), 1, self.color)
        where.blit(self.number, (self.x, self.y))

# класс ящика, состоит из GAME ячеек с цифрами и одной пустой в конце

class Box:
    def __init__(self):
        self.box = [Block(DIGIT_COLOR, i+1, (i % BLOCKS_IN_LINE) * BLOCK_SIZE, (i // BLOCKS_IN_LINE) * BLOCK_SIZE) for i in range(GAME)]
        self.box.append(Block(DIGIT_COLOR, ' ', (GAME % BLOCKS_IN_LINE) * BLOCK_SIZE, (GAME // BLOCKS_IN_LINE) * BLOCK_SIZE))
        self.empty = GAME + 1

# отрисовка ящика

    def render(self, where):
        for i in range(GAME+1):
            self.box[i].render(where)

# движение блоков, если пустой блок и вызванный рядом по горизонтали и вертикали, то поменять их местами

    def move(self, digit):
        if abs(digit - self.empty) == 1 or abs(digit - self.empty) == BLOCKS_IN_LINE:
            self.box[self.empty-1].digit, self.box[digit-1].digit = self.box[digit-1].digit, self.box[self.empty-1].digit
            self.empty = digit

# если все номера блоков упорядочены, то игра выиграна

    def win(self):
        if list(self.box[i].digit for i in range(GAME)) == list(range(1, GAME+1)):
            print("You win!")
            return True
        return False

# чтоб перемешать ящик, RANDOM раз случайным образом тыкаем в какие-то блоки

    def shuffle(self):
        for i in range(RANDOM):
            self.move(random.randint(1, GAME+1))

# главная функция - процесс игры

def main():

    exit = False

    box = Box()
    box.shuffle()

    while not exit:

# фон, без картинки, отрисовка ящика

#        fon = pygame.image.load(BACKGROUND)
        fon = pygame.Surface((SCREEN_X, SCREEN_Y))
        fon.fill(BACKGROUND_COLOR) 

        screen.blit(fon, (0, 0))

        box.render(screen)

# блок управления. глобальный выход из цикла и из игры без результата по нажатию крестика, 
# при нажатии мышки определить ее координаты, перевести их в номер ячейки, сдвинуть блок,
# проверить, не выиграли ли мы

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()                      
                digit = (pos[0] // BLOCK_SIZE % BLOCKS_IN_LINE) + (pos[1] // BLOCK_SIZE % BLOCKS_IN_LINE)*BLOCKS_IN_LINE + 1 
                box.move(digit)
                if box.win(): 
                    exit = True

        window.blit(screen, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':

# создаем главное окно, даем ему название, создаем экран на главном окне

    window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Питнашки')
    screen = pygame.Surface((SCREEN_X, SCREEN_Y))

# запускаем игру

    main()
