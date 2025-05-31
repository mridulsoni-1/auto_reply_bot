import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyBFGjgyPFIvlhT5ObtL9lNpMiVSApCZ33c")

# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
chat = model.start_chat()

# Wait before starting (optional: gives you time to switch windows)
time.sleep(2)

def is_last_message_from_sender(chat_log: str, sender_name: str) -> bool:
    lines = chat_log.strip().split('\n')
    for line in reversed(lines):
        if '] ' in line:
            try:
                sender = line.split('] ')[1].split(':')[0].strip()
                if sender == sender_name:
                    return True
                elif sender:  # Found a different sender, stop checking
                    return False
            except IndexError:
                continue
    return False

# Step 1: Click on the icon (adjust coordinates as needed)
pyautogui.click(504, 1750)
time.sleep(2)

while True:
    # Step 2: Drag from start to end position to select text
    pyautogui.moveTo(1048, 311)
    pyautogui.mouseDown()
    pyautogui.moveTo(2722, 1539, duration=1.5)  # Smooth drag
    pyautogui.mouseUp()

    # Step 3: Copy selected text using Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for clipboard to update
    pyautogui.click(1048, 311)  # Optional: re-focus

    # Step 4: Get clipboard text into a variable
    chat_history = pyperclip.paste()

    print("Copied Text:")
    print(chat_history)

    if is_last_message_from_sender(chat_history, sender_name="your_contact_with_whom_you_want_chat"):
        persona = (
            "You are Mridul, an Indian coder who talks naturally mixing Hindi and English (Hinglish). "
            "You respond casually, like a friend chatting. "
            "Keep answers relevant, clear, and friendly with a chill tone. "
            "Never copy example text or irrelevant content. "
            "Only respond with the next message as Mridul would say it."
        )

        chat.send_message(persona)

        # Step 6: Send the chat history as user input
        response = chat.send_message(chat_history)

        # Step 7: Print the response
        print("Mridul:", response.text)

        # Copy the actual text content to clipboard
        pyperclip.copy(response.text)

        time.sleep(2)  # Time to switch to the target window

        # Click at (1249, 1629)
        pyautogui.click(1249, 1629)

        # Paste clipboard content (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')

        # Press Enter
        pyautogui.press('enter')
