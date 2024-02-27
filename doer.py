import pyautogui
import time
import logging

def simulate_action(action):
    if "Key pressed" in action:
        key = action.split(": ")[-1]
        if key.startswith("'") and key.endswith("'"):
            pyautogui.press(key.strip("'").replace("''", "'"))
        elif "space" in key:
            pyautogui.press('space')
        elif "enter" in key:
            pyautogui.press('enter')
        # Omitimos el manejo de Key.shift_r aquí; si necesitas manejar mayúsculas o caracteres especiales,
        # deberías hacerlo con una lógica que considere el estado de las teclas modificadoras.
    elif "Mouse clicked at" in action:
        coords = action.split(" at: ")[1].split(")")[0]  # Ajuste aquí
        x, y = map(int, coords.strip("()").split(", "))
        pyautogui.click(x, y)


def simulate_actions(filename):
    with open(filename, 'r') as file:
        for line in file:
            simulate_action(line.strip())
            time.sleep(0.25)  # Ajusta este tiempo si es necesario para replicar la acción

simulate_actions("activity_log.txt")
