import pyautogui
import time

def move_mouse():
    # Définir le décalage pour chaque mouvement
    offset = 100
    while True:
        # Obtenir la position actuelle de la souris
        x, y = pyautogui.position()
        
        # Déplacer la souris vers la droite
        pyautogui.moveTo(x + offset, y)
        time.sleep(5)
        
        # Déplacer la souris vers le bas
        pyautogui.moveTo(x + offset, y + offset)
        time.sleep(5)
        
        # Déplacer la souris vers la gauche
        pyautogui.moveTo(x, y + offset)
        time.sleep(5)
        
        # Déplacer la souris vers le haut pour revenir à la position initiale
        pyautogui.moveTo(x, y)
        time.sleep(5)

if __name__ == "__main__":
    move_mouse()
