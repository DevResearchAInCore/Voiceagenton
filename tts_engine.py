import edge_tts
import asyncio
import uuid
import pygame
import os
import time

async def generate_voice(text, filename):

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(filename)

def speak(text):

    filename = f"voice_{uuid.uuid4()}.mp3"

    asyncio.run(generate_voice(text, filename))

    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=22050, size=-16, channels=2)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()

    try:
        os.remove(filename)
    except:
        pass
