# Speech-to-Text Transcription Script

This script uses the Vosk speech recognition toolkit to transcribe audio files into text and saves the transcription in a Word document (.docx). 

## Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **Vosk Model**: Download the Vosk model for speech recognition from [Vosk Models](https://alphacephei.com/vosk/models).
3. **Required Python Libraries**: Install the necessary Python libraries using the following command:
    ```bash
    pip install vosk python-docx
    ```

## How It Works

1. The script checks if the Vosk model exists in the specified path.
2. It opens the provided audio file and reads the audio data.
3. The audio data is processed using Vosk's speech recognition to transcribe the speech into text.
4. The transcribed text is saved into a new Word document (`transcript.docx`).

## Usage

1. **Download and Install Dependencies**: 
    ```bash
    pip install vosk python-docx
    ```
2. **Download a Vosk Model**: Download a Vosk model (e.g., `vosk-model-en-us-0.42-gigaspeech`) from the [Vosk website](https://alphacephei.com/vosk/models) and extract it to a directory.

3. **Update the Model Path**: Replace the placeholder in the script with the path to your downloaded Vosk model:
    ```python
    model_path = "{your path of the downloaded model}/vosk-model-en-us-0.42-gigaspeech"
    ```

4. **Run the Script**:
    - Ensure your audio file is accessible.
    - Run the script and provide the path to your audio file when prompted.
    - The script will transcribe the audio and save the transcription as `transcript.docx`.

    ```bash
    python your_script_name.py
    ```

5. **Example**:
    ```
    Enter the path to your audio file: /path/to/your/audio/file.wav
    ```

    After successful transcription, a file named `transcript.docx` will be created in the same directory as the script.

## Error Handling

- **Vosk Model Not Found**: Ensure the model path is correct and the model exists at the specified location.
- **Audio File Not Found**: Verify the audio file path is correct.
- **File Permission Error**: Ensure you have write permissions in the directory where the script is saving the transcription.

## Notes

- Adjust the sample rate in the `KaldiRecognizer` instantiation if your audio file's sample rate differs from 16000 Hz.
- The script currently handles basic error scenarios. For production use, consider adding more comprehensive error handling and logging.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize and extend this script to better fit your specific needs!
