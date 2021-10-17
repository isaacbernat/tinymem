import thumby
import random
import time

thumby.display.fill(0)
thumby.display.drawText("TinyMem", 8, 0, 1)
thumby.display.drawText("easy:A/B", 0, 8, 1)
thumby.display.drawText("hard:arrw", 0, 16, 1)
thumby.display.drawText("ONLY EASY", 0, 32, 1)
thumby.display.update()

# TODO use this to select easy vs hard
while(thumby.actionPressed() == True):
    pass
while(thumby.actionPressed() == False):
    pass


sequence = [random.randint(0, 1) for i in range(10)]
max_pos = 0

game_running = True

MEM_KEYS = ["A", "B"]  # TODO sth to display bigger on screen
DELAY_MS = 1000


def print_sequence():
    pass  # TODO


def ask_sequence():
    pass  # TODO


def game_over():
    pass  # TODO


while(game_running == True):
    pre_print_time = time.ticks_ms()
    thumby.display.fill(0)
    thumby.display.drawText("WAIT NEXT", 0, 0, 1)
    thumby.display.drawText("ITERATION", 0, 8, 1)
    thumby.display.drawText(str(max_pos), 0, 16, 1)
    thumby.display.drawText(str(sequence), 0, 32, 1)
    thumby.display.update()
    max_pos += 1
    while(time.ticks_ms() - pre_print_time < DELAY_MS):
        pass
