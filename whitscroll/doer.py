import pyautogui
import time

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
    elif "Mouse scrolled at" in action:
        action_parts = action.split(" ")
        coords_part = action_parts[4]  # Obtiene la parte de la cadena que contiene las coordenadas
        delta_part = action_parts[9]  # Obtiene la parte de la cadena que contiene los deltas
        x, y = map(int, coords_part.strip("():").split(","))
        dx, dy = map(int, delta_part.strip("():").split(","))
        pyautogui.scroll(dy * 10, x, y)  # Multiplicamos dy por un factor para aumentar el efecto del scroll

def simulate_actions(filename):
    with open(filename, 'r') as file:
        for line in file:
            simulate_action(line.strip())
            time.sleep(0.25)  # Ajuste el tiempo según sea necesario

simulate_actions("activity_log.txt")
