# tinymem
[Thumby](https://thumby.us/) Simon-inspired game where players test their tiny short term memory.

[tinymem_video.webm](https://user-images.githubusercontent.com/2509809/183149073-1338aad7-a044-4f8b-9d0f-7ac3a8d719fc.webm)

## how to play?
- Repeat key sequences (hard->arrows; easy->buttons) following sounds and screen indications.
- You can try it on a [Thumby emulator here](https://code.thumby.us/)

https://user-images.githubusercontent.com/2509809/183148998-b59710fb-eb5c-4f07-8ce5-5c32f16d5ef1.mp4

## why?
I wanted to create a game as a Proof of Concept that:

- Is simple to understand (code):
    - Less than 50 lines of MicroPython (not PEP8-compliant though ^_^').
    - No single function is over a dozen lines.
    - Maximum code nesting depth is 3.
    - Could be used as an example/inspiration of how easy it is to program/make games ;D.

- Is simple to play:
    - The game this is based on has been around for decades and is already part of popular culture.
    - Since it's turn based, it doesn't depend on hand dexterity, coordination or fast reaction times.

- Uses many Thumby features:
    - Audio (had to play around different frequency bands. Many are inaudible at arms distance).
    - D-pad.
    - Buttons (for those who like to think in binary :D).
    - Sprites (non-moving, and just one ^_^).
    - Text (using default font).
    - Link Cable... ok this I haven't... I couldn't decide between a couple of ideas:
        - a) one player, two controllers. That is: not only which button matters, but also which Thumby you click!
        - b) versus game, one player choses the new element of the sequence every time. That is, instead of being random.
    - Did I miss sth relevant? E.g. setting a different CPU clock frequency.
