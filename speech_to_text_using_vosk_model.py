import os
import vosk
import docx

# Model path (replace with your downloaded Vosk model path)
model_path = "{your path of the downloaded model}/vosk-model-en-us-0.42-gigaspeech"

def recognize_audio(audio_filepath):
  """
  Recognizes speech from an audio file using Vosk.

  Args:
      audio_filepath (str): Path to the audio file.

  Returns:
      str: The transcribed text, or None if an error occurs.
  """

  # Check if Vosk model exists
  if not os.path.exists(model_path):
    print(f"Vosk model not found at '{model_path}'. Download a model from https://alphacephei.com/vosk/")
    return None

  # Create Vosk model
  model = vosk.Model(model_path)

  # Open audio file
  try:
    with open(audio_filepath, "rb") as f:
      # Read audio data
      audio_data = f.read()
  except FileNotFoundError:
    print(f"Error: Audio file '{audio_filepath}' not found.")
    return None

  # Create Vosk recognizer
  rec = vosk.KaldiRecognizer(model, 16000)  # Sample rate of your audio (might need adjustment)

  # Feed audio data to recognizer
  rec.AcceptWaveform(audio_data)

  # Get text result
  text = rec.Result()

  # Check if recognition successful
  if text == "<unk>":
    print("Speech recognition failed.")
    return None

  return text


# Get audio file path from user
audio_filepath = input("Enter the path to your audio file: ")

# Recognize audio
transcription = recognize_audio(audio_filepath)

# Check if transcription successful
if transcription:
  # Create a new docx document
  doc = docx.Document()

  # Add a paragraph with the transcribed text
  paragraph = doc.add_paragraph(transcription)

  # Save the document as transcript.docx
  try:
    doc.save("transcript.docx")
    print("Transcription saved to transcript.docx")
  except PermissionError:
    print("Error: Could not save transcript.docx. Check file permissions.")
else:
  print("Transcription failed.")