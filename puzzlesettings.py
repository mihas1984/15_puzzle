# ���������� ������� �������� ���� � ������, ������� ����� �������������� � ����, 
# ������� ����� ����� � ����� �������/�������, ������ ��� ����� �������,
# ������� �� ����� �����

SCREEN_X = 300
SCREEN_Y = SCREEN_X

BLOCKS_IN_LINE = 4
BLOCK_SIZE = SCREEN_X // BLOCKS_IN_LINE

GAME = BLOCKS_IN_LINE*BLOCKS_IN_LINE - 1

# ������ ���� ���� � �����

#BACKGROUND = 'fon.png'
BACKGROUND_COLOR = (255, 255, 255)
DIGIT_COLOR = (0, 0, 0)

# ������� ��� ����� �������� ����, �������� ��������� �� ���� ���������� BLOCKS_IN_LINE

RANDOM = 10**(BLOCKS_IN_LINE-1)

# �������������� ������

FONT_OF_DIGITS = "comicsansms"
DIGIT_SIZE = BLOCK_SIZE//2

