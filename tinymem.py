import thumby
import random
import time


sequence = []
max_pos = 0

game_running = True

MEM_KEYS = ["A", "B"]  # TODO sth to display bigger on screen
DELAY_MS = 1000


def wait(init_time=None, duration_ms=1000):
    init_time = time.ticks_ms() if not init_time else init_time
    while(time.ticks_ms() - init_time < duration_ms):
        pass


def init_game():
    global sequence, max_pos
    thumby.display.fill(0)
    thumby.display.drawText("TinyMem", 8, 0, 1)
    thumby.display.drawText("easy:A/B", 0, 8, 1)
    thumby.display.drawText("hard:arrw", 0, 16, 1)
    thumby.display.drawText("ONLY EASY", 0, 32, 1)
    thumby.display.update()
    sequence = [random.randint(0, 1) for i in range(10)]
    max_pos = 0


def getcharinputNew():
    if(thumby.buttonL.justPressed()):
        return 'L'
    if(thumby.buttonR.justPressed()):
        return 'R'
    if(thumby.buttonU.justPressed()):
        return 'U'
    if(thumby.buttonD.justPressed()):
        return 'D'
    if(thumby.buttonA.justPressed()):
        return 0
    if(thumby.buttonB.justPressed()):
        return 1
    return None


def wait_press():
    while(getcharinputNew() is None):
        pass


def print_sequence():
    thumby.display.fill(0)
    thumby.display.drawText("watch key", 0, 0, 1)
    thumby.display.drawText("sequence", 0, 8, 1)
    thumby.display.drawText("CAREFULLY", 0, 16, 1)
    thumby.display.drawText("press ANY", 0, 32, 1)
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


def game_over():
    thumby.display.fill(0)
    thumby.display.drawText("GAME OVER", 0, 0, 1)
    thumby.display.drawText("your mem=", 0, 8, 1)
    thumby.display.drawText(str(max_pos), 0, 16, 1)
    thumby.display.drawText("bits", 0, 24, 1)
    thumby.display.drawText("press ANY", 0, 32, 1)
    thumby.display.update()
    wait_press()
    pass


def ask_sequence():
    thumby.display.fill(0)
    thumby.display.drawText("your turn", 0, 0, 1)
    thumby.display.drawText("repeat!", 0, 8, 1)
    thumby.display.update()

    current_pos = 0
    while (current_pos <= max_pos):
        c = getcharinputNew()
        if c is None:
            continue

        if c == sequence[current_pos]:
            current_pos += 1
            thumby.display.fill(0)
            thumby.display.drawText("correct!", 0, 0, 1)
            thumby.display.drawText(str(c), 0, 8, 1)
            thumby.display.update()
            wait()
        else:
            game_over()
            break
    return


init_game()
wait_press()  # TODO use this to select easy vs hard
while(game_running):
    print_sequence()
    ask_sequence()
    max_pos += 1
