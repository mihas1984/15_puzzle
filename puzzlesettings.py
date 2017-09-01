# определ€ем размеры игрового пол€ и шрифта, который будет использоватьс€ в игре, 
# сколько будет €чеек в одной колонке/столбце, какого они будут размера,
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

# сколько раз будем тасовать поле, значение увеличить по мере увеличени€ BLOCKS_IN_LINE

RANDOM = 10**(BLOCKS_IN_LINE-1)

# инициализируем шрифты

FONT_OF_DIGITS = "comicsansms"
DIGIT_SIZE = BLOCK_SIZE//2

