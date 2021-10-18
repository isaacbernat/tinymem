import thumby
import random
import time


sequence = []
max_pos = 0
difficulty = 0

MEM_KEYS = ["A", "B", "UP", "RIGHT", "DOWN", "LEFT"]  # TODO bigger onscreen
DELAY_MS = 1000


def wait(init_time=None, duration_ms=1000):
    init_time = time.ticks_ms() if not init_time else init_time
    while(time.ticks_ms() - init_time < duration_ms):
        pass


def print_text(lines):
    thumby.display.fill(0)
    for index, content in enumerate(lines):
        thumby.display.drawText(content, 0, 8 * index, 1)
    thumby.display.update()


def init_game():
    global max_pos, difficulty, sequence
    print_text([" TinyMem", "easy:A/B", "hard:arrw", "by:Isaac", "   Bernat"])
    random.seed(time.ticks_ms())
    max_pos = - 1
    c = wait_press()
    if c < 2:
        difficulty = 1
        sequence = [random.randint(0, 1) for i in range(100)]
    else:
        difficulty = 2
        sequence = [random.randint(2, 5) for i in range(100)]


def getcharinputNew():
    if(thumby.buttonA.justPressed()):
        return 0
    if(thumby.buttonB.justPressed()):
        return 1
    if(thumby.buttonU.justPressed()):
        return 2
    if(thumby.buttonR.justPressed()):
        return 3
    if(thumby.buttonD.justPressed()):
        return 4
    if(thumby.buttonL.justPressed()):
        return 5
    return None


def wait_press():
    c = getcharinputNew()
    while(c is None):
        c = getcharinputNew()
    return c


def print_sequence():
    print_text(["watch key", "sequence", "CAREFULLY", "", "press ANY"])
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
    print_text(["GAME OVER", "your mem=", f"{str(max_pos*difficulty)} bits", "", "press ANY"])
    wait_press()
    init_game()


def ask_sequence():
    print_text(["your turn", "repeat"])
    current_pos = 0
    while (current_pos <= max_pos):
        if sequence[current_pos] == wait_press():
            current_pos += 1
            thumby.display.fill(0)
            thumby.display.drawText("correct!", 0, 0, 1)
            thumby.display.drawText(f"{current_pos} done" , 0, 8, 1)
            thumby.display.drawText(f"{max_pos - current_pos + 1} left" , 0, 16, 1)
            thumby.display.update()
        else:
            game_over()
            break
    return


init_game()
max_pos += 1
while(True):
    print_sequence()
    ask_sequence()
    max_pos += 1
