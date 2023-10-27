import openai

# Set your OpenAI API key
openai.api_key = "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"

# Load the audio file
audio_file = open("C:/Users/kris_/Python/API/aieng.mp3", "rb")

# Transcribe the audio file using OpenAI's Whisper API
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Extract and print the transcribed text
print(transcript['text'])

# Save the transcribed text to a text file
with open("transcription2.txt", "w") as text_file:
    text_file.write(transcript['text'])
