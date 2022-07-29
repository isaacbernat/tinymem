import random, time, thumby, collections


controls_map = bytearray([224,32,32,32,32,63,1,1,1,1,1,1,1,1,1,63,32,32,32,32,224,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,1,1,1,1,1,1,1,255,
                          255,128,128,128,128,128,0,0,0,0,0,0,0,0,0,128,128,128,128,128,255,0,0,0,0,0,0,0,0,0,252,4,4,4,4,4,4,4,252,0,7,4,4,4,4,4,4,4,7,
                          0,0,0,0,0,31,16,16,16,16,16,16,16,16,16,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,16,16,16,16,16,16,16,31,0,0,0,0,0,0,0,0,0,0])
controls_sprite = thumby.Sprite(49, 21, controls_map, 10, 10)  # sprite based on Laveréna Wienclaw
Button = collections.namedtuple("Button", "letter freq x y")  # TODO try freq around 5000-6000hz
MEM_KEYS = [Button("", 20, 0, 0), Button("A", 440, 52, 12), Button("B", 330, 42, 22), Button("U", 659, 18, 12), Button("R", 554, 24, 17), Button("D", 440, 18, 22), Button("L", 330, 12, 17)]


def print_sprite(val=0, text=["", "", "", "", ""]):
    thumby.display.fill(0)
    for index, content in enumerate(text):
        thumby.display.drawText(content, 0, 8 * index, 1)
    thumby.display.drawSprite(controls_sprite)
    thumby.display.drawText(MEM_KEYS[val].letter, MEM_KEYS[val].x, MEM_KEYS[val].y, 1)
    thumby.display.update()
    thumby.audio.playBlocking(MEM_KEYS[val].freq, val == 0 or 1000)


def init_game():
    print_sprite(text=["  Tiny Mem!", "", "", "", "  hard;easy"])
    random.seed(time.ticks_ms())
    value_range = (1, 2) if wait_press() < 3 else (3, 6)
    return 0, [random.randint(*value_range) for i in range(100)]


def wait_press(c=None):
    while(c is None):
        c = (thumby.buttonL.justPressed() and 6) or (thumby.buttonD.justPressed() and 5) or (thumby.buttonR.justPressed() and 4) or (thumby.buttonU.justPressed() and 3) or (thumby.buttonB.justPressed() and 2) or (thumby.buttonA.justPressed() and 1) or None
    return c


def print_sequence(max_pos, sequence):
    for index, val in enumerate(sequence[:max_pos + 1]):
        print_sprite(val=val, text=[f"  key={MEM_KEYS[val].letter}", "", "", "", f"  num={index + 1}"])
        init_time = time.ticks_ms()


def ask_sequence(max_pos, sequence, current_pos=0):
    print_sprite(text=["  your turn", "", "", "", "  repeat"])
    while (current_pos <= max_pos):
        if sequence[current_pos] != wait_press():  # GAME OVER
            print_sprite(text=["  your mem=", "", "", "", f"  {str(max_pos*(min(sequence) == 1 or 2))} bits"])
            wait_press()
            return init_game()
        current_pos += 1
        print_sprite(val=sequence[current_pos - 1], text=[f"  {current_pos} done", "", "", "", f"  {max_pos - current_pos + 1} left"])
    return max_pos + 1, sequence


max_pos, sequence = init_game()
while(True):
    print_sequence(max_pos, sequence)
    max_pos, sequence = ask_sequence(max_pos, sequence)
