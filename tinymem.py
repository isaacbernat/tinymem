import thumby
import random
import time

thumby.display.fill(0)
thumby.display.drawText("TinyMem", 8, 0, 1)
thumby.display.drawText("easy:A/B", 0, 8, 1)
thumby.display.drawText("hard:arrw", 0, 16, 1)
thumby.display.drawText("ONLY EASY", 0, 32, 1)
thumby.display.update()


sequence = [random.randint(0, 1) for i in range(10)]
max_pos = 0

game_running = True

MEM_KEYS = ["A", "B"]  # TODO sth to display bigger on screen
DELAY_MS = 1000


def wait(init_time=None, duration_ms=1000):
    init_time = time.ticks_ms() if not init_time else init_time
    while(time.ticks_ms() - init_time < duration_ms):
        pass


def wait_press():
    while(thumby.actionPressed()):
        pass
    while(not thumby.actionPressed()):
        pass


def print_sequence():
    thumby.display.fill(0)
    thumby.display.drawText("watch key", 0, 0, 1)
    thumby.display.drawText("sequence", 0, 8, 1)
    thumby.display.drawText("CAREFULLY", 0, 16, 1)
    thumby.display.drawText("press A/B", 0, 32, 1)
    thumby.display.update()
    wait_press()

    for index, val in enumerate(sequence):
        if index > max_pos:
            break
        # TODO play audio
        thumby.display.fill(0)
        thumby.display.drawText(MEM_KEYS[val], 4 * index, 16, 1)
        thumby.display.update()
        wait()


def ask_sequence():
    thumby.display.fill(0)
    thumby.display.drawText("repeat", 0, 0, 1)
    thumby.display.update()
    wait()

    current_post = 0
    while (current_post < max_pos):
        pass


def game_over():  # TODO
    thumby.display.fill(0)
    thumby.display.drawText("GAME OVER", 0, 0, 1)
    thumby.display.drawText("your mem=", 0, 8, 1)
    thumby.display.drawText(str(max_pos), 0, 16, 1)
    thumby.display.drawText("bits", 0, 24, 1)
    thumby.display.drawText("press A/B", 0, 32, 1)
    thumby.display.update()
    wait_press()
    pass


# TODO use this to select easy vs hard
wait_press()
while(game_running):
    print_sequence()
    max_pos += 1
