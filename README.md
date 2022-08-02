# tinymem
[Thumby](https://thumby.us/) Simon-inspired game where players test their tiny short term memory.

## how to play?
- Repeat key sequences (hard->arrows; easy->buttons) following music and screen indications.
- You can try it on a [Thumby emulator here](https://code.thumby.us/)

## why?
I wanted to create a game as a Proof of Concept that:

- Was simple to understand (code):
    - Less than 50 lines of MicroPython (not PEP8-compliant though ^_^').
    - No single function is over a dozen lines.
    - A single nested conditional/loop.
    - Could be used as an example/inspiration of how easy it is to program/make games ;D.

- Was simple to play:
    - The game this is based on has been around for decades and is already part of popular culture.
    - Since it's turn based, it doesn't depend on hand dexterity, coordination or fast reaction times.

- Used many Thumby features:
    - Audio (had to play around different frequency bands. Many are inaudible at arms distance).
    - D-pad.
    - Buttons (for those who like to think in binary :D).
    - Sprites (non-moving, and just one ^_^).
    - Text (using default font).
    - Link cable... ok this I haven't... I couldn't decide between a couple of ideas:
        - a) the game playable in both boards. That is: not only which button, but which Thumby is relevant!
        - b) versus game, one player choses the sequence for the other instead of being random.
    - Did I miss sth? E.g. setting a different CPU clock frequency
