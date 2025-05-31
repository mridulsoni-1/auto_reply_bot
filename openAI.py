import google.generativeai as genai

# Configure with your Gemini API key
genai.configure(api_key="AIzaSyBFGjgyPFIvlhT5ObtL9lNpMiVSApCZ33c")

# Initialize model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Start chat session
chat = model.start_chat()

# Inject system-level instruction (Harry’s personality)
persona = (
    "You are Mridul, an Indian coder who speaks both Hindi and English. "
    "You are friendly, helpful, and respond casually like you're chatting with a friend. "
    "Mix light Hindi with English and keep a chill, funny tone. Always respond like Mridul."
)
chat.send_message(persona)
# Now the latest user input (from your `command` variable)
command = '''[1:21 PM, 5/29/2025] Mridul Soni: Haaan
[1:21 PM, 5/29/2025] Eshan: Groq
[1:21 PM, 5/29/2025] Mridul Soni: Theek hai
[11:46 PM, 5/29/2025] Mridul Soni: Maan ja insta uspe bbi hai mera 😩
[12:13 AM, 5/30/2025] Eshan: Ftttt gyiii gaand
[12:13 AM, 5/30/2025] Mridul Soni: Haaan bhyi mere pass nhi aaegi itti jldi
[12:14 AM, 5/30/2025] Eshan: Thike
😭
[12:14 AM, 5/30/2025] Mridul Soni: Haan'''
response = chat.send_message(command)

# Print the output
print("Harry:", response.text)
