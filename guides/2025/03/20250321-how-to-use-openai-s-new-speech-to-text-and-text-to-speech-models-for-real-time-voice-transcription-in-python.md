# How to Use OpenAI's New Speech-to-Text and Text-to-Speech Models for Real-Time Voice Transcription in Python

This comprehensive guide walks you through setting up a powerful voice transcription system that automatically converts your speech to text and pastes it into any application. The system uses OpenAI's advanced speech models for high-quality transcription and optional text-to-speech playback.

Prerequisites:
- Basic familiarity with Python and Keyboard Maestro
- Understanding of API integration concepts
- An active OpenAI API key with appropriate credits

## Development Context

I developed this tool as part of my OpenAI Agents learning project to explore OpenAI's latest voice capabilities. The design process involved collaborative brainstorming with AI assistants in both Cursor and WindSurf IDEs(yes, I'm also testing out WindSurf). The implementation incorporates:

1. **Intelligent Silence Detection**: A sophisticated state machine approach that automatically stops recording after detecting a pause in speech.
2. **OpenAI Model Integration**: Leverages the most advanced OpenAI models for both transcription and text-to-speech.
3. **Keyboard Maestro Automation**: Streamlines the workflow with hotkey triggers and automatic clipboard management.

The tool addresses common challenges in voice recording:
- Premature stopping during natural speech pauses
- Determining when speech is truly complete
- Providing clear visual feedback during recording
- Seamless integration with macOS workflow

## System Components

1. **Voice Recording Script**: `stt-2-tts-km.py` handles audio recording with smart silence detection
2. **Transcription**: Uses OpenAI's `gpt-4o-transcribe` model
3. **Playback**: Optional TTS playback with `gpt-4o-mini-tts`
4. **Keyboard Maestro**: Triggers the workflow and handles text pasting

## Silence Detection System

The tool employs a three-state machine approach for recording:

1. **WAITING_FOR_SPEECH**: Initial listening for audio above threshold
2. **RECORDING**: Active recording of speech
3. **MONITORING_SILENCE**: Tracking silence duration to determine when to stop

This approach effectively captures complete thoughts even with brief hesitations and provides visual feedback during the recording process.

## Setup Instructions

### 1. Prerequisites

- macOS
- Python 3.8+ with required packages
- OpenAI API key
- Keyboard Maestro application or any other automation tool that supports shell scripts
- portaudio (system dependency)

### 2. Install Dependencies

```bash
# Install Python packages
pip install openai pyaudio pyperclip python-dotenv

# Install system dependency if needed
brew install portaudio
```

### 3. Configure API Key

Create a `.env` file in the project directory with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Python Environment Configuration

The script uses a shebang line to ensure compatibility with Keyboard Maestro:
```python
#!/path/to/your/python/interpreter 
```

You may need to adjust this path to match your Python environment. This ensures:
- Consistent execution regardless of working directory
- Reliable launch from Keyboard Maestro
- Access to all necessary packages

### 5. Keyboard Maestro Macro Setup

1. **Create a new macro** in Keyboard Maestro
2. **Set a trigger** (e.g., keyboard shortcut like ⌘⇧V)
3. **Add an "Execute Shell Script" action** with:

```bash
/bin/zsh -c "path/to/your/script.py -s 3 -m 30 -p true -v Shimmer"
```

This is the command to run the script with the following parameters:
- `-s 3`: Set silence threshold to 3 seconds
- `-m 30`: Set maximum recording time to 30 seconds
- `-p true`: Enable TTS playback
- `-v Shimmer`: Use the "Shimmer" voice

4. **Add a "Paste" action** immediately after the script execution

### 6. Customizing the Experience

The script accepts several command-line arguments:

```bash
# Example with 2-second silence threshold and echo voice
/bin/zsh -c "/Users/wankyuchoi/Library/CloudStorage/Dropbox/cwkPersonalProjects/cwkOpenAIAgents/voice/stt-2-tts-km.py -s 2 -v Onyx"
```

- `-s SECONDS` or `--silence SECONDS`: Set silence threshold (default: 3)
- `-m SECONDS` or `--max-duration SECONDS`: Set maximum recording time (default: 60)
- `-v VOICE` or `--voice VOICE`: Select TTS voice (default: onyx)
  Available options: alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer, verse
- `-d` or `--debug`: Enable debug mode for verbose output
- `--no-playback`: Disable TTS playback

## Keyboard Maestro Macro Example

![Keyboard Maestro Macro](images/20250321-01.png)
> *Keyboard Maestro Macro*

The following explains a complete Keyboard Maestro macro implementation:

### How the Keyboard Maestro Macro Works

This macro creates a seamless voice-to-text workflow by connecting several components:

1. **Trigger**: The macro is activated with the OPT+CMD+V keyboard shortcut (⌥⌘V) - a single press initiates the entire workflow.

2. **Display Text Action**: Shows a large "Recording...(Pause for a second and start speaking...)" message. This gives you visual feedback that recording is about to begin and prepares you to speak.

3. **Execute Shell Script Action**: This is where the real magic happens! The command:
   ```
   /bin/zsh -c "/Users/wankyuchoi/Library/CloudStorage/Dropbox/cwkPersonalProjects/cwkOpenAIAgents/voice/stt-2-tts-km.py -s 3 -p true -v Shimmer"
   ```
   Does several things:
   - Runs your Python script with specific parameters
   - `-s 3`: Sets silence threshold to 3 seconds
   - `-p true`: Enables TTS playback
   - `-v Shimmer`: Uses the "Shimmer" voice for text-to-speech

4. **Paste Action**: After the script finishes, this action automatically pastes the transcribed text (which was copied to clipboard by the script) into wherever your cursor is positioned.

The workflow is particularly clever because:
- The script handles all the complex operations (recording, silence detection, API calls)
- But Keyboard Maestro provides the automation wrapper that makes it feel seamless
- Your visual feedback + automatic paste action creates a complete user experience

When you trigger this with the shortcut, it all happens in sequence - show message, record your voice, process through OpenAI's models, and paste the result right where you need it!

## Usage Workflow

1. **Position cursor** where you want text to appear
2. **Trigger the macro** using your shortcut
3. **Speak clearly** - a sound will indicate recording has started
4. **Pause when finished** - recording stops after your set silence period
5. **Wait briefly** for processing and transcription
6. **Review the pasted text** and edit if needed

## Privacy Considerations

- Audio files are temporarily stored in `/tmp` and deleted after use
- Audio is processed through OpenAI's API and subject to their privacy policy
- No permanent storage of audio recordings
- API keys are stored securely in an environment file

## Troubleshooting

- If the script doesn't work when launched via `./stt-2-tts-km.py`, try running it with an explicit Python command: `python stt-2-tts-km.py`
- If you encounter package not found errors, ensure all dependencies are installed in your active Python environment
- For silence detection issues, try enabling debug mode and adjusting the silence threshold

That's it! Your spoken words will appear like magic in any text field.

## Source Code

Below is the complete source code for the `stt-2-tts-km.py` script:

```python
#!/opt/anaconda3/envs/openaiagents/bin/python
"""
Voice Recording and Transcription Tool for Keyboard Maestro

This script:
1. Plays a sound to indicate recording has begun
2. Records audio from your microphone automatically
3. Stops recording after detecting silence or reaching max duration
4. Transcribes it using OpenAI's gpt-4o-transcribe model
5. Reads the transcription back using gpt-4o-mini-tts (optional)
6. Copies the transcription to the system clipboard
7. Cleans up temporary files

Dependencies:
- openai
- pyaudio
- pyperclip
- python-dotenv

Command-line arguments:
-s, --silence SECONDS: Set silence threshold in seconds (default: 3)
-m, --max-duration SECONDS: Set maximum recording duration in seconds (default: 60)
-p, --play-back true/false: Whether to play back the transcription (default: true)
-v, --voice VOICE: TTS voice to use (default: onyx, options: alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer, verse)
"""

import os
import sys
import time
import tempfile
import argparse
import wave
import pyaudio
import pyperclip
import subprocess
import math
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()

# Debug mode for verbose output
DEBUG = False

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 200  # Lower threshold for better speech detection

def is_silent(data_chunk, threshold=THRESHOLD):
    """Check if an audio chunk is silent based on amplitude"""
    # Convert audio to numpy array
    audio_data = np.frombuffer(data_chunk, dtype=np.int16)
    
    # Calculate absolute amplitude
    amplitude = np.abs(audio_data).mean()
    
    # Simple threshold check
    is_silence = amplitude < threshold
    
    if DEBUG:
        print(f"Amplitude: {amplitude:.2f}, Threshold: {threshold}, Silent: {is_silence}")
        
    return is_silence

def record_audio(filename, silence_seconds=3, max_duration=60):
    """Record audio until silence is detected or max duration is reached"""
    print(f"Recording to {filename}...")
    print(f"Will stop after {silence_seconds} seconds of silence or {max_duration} seconds max")
    
    # Open the audio stream
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    # Play a sound to indicate recording has begun
    subprocess.run(["afplay", "/System/Library/Sounds/Tink.aiff"], check=False)
    print("Recording started...")
    
    # Initialize variables
    frames = []
    silence_start_time = None
    start_time = time.time()
    recording_state = "WAITING_FOR_SPEECH"  # States: WAITING_FOR_SPEECH, RECORDING, SILENCE_DETECTED
    
    # Record until silence is detected or max duration is reached
    try:
        while True:
            # Read audio data
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            
            current_time = time.time()
            is_silent_chunk = is_silent(data)
            
            # STATE: Waiting for speech
            if recording_state == "WAITING_FOR_SPEECH":
                if not is_silent_chunk:
                    # If we detect speech, transition to RECORDING state
                    recording_state = "RECORDING"
                    print("Speech detected - recording started")
                # Only transition to silence tracking after 15 seconds of no initial speech
                elif current_time - start_time > 15:
                    recording_state = "SILENCE_DETECTED"
                    silence_start_time = current_time
                    print("No initial speech detected after 15 seconds - beginning silence countdown")
            
            # STATE: Recording active speech
            elif recording_state == "RECORDING":
                if is_silent_chunk:
                    # If silence detected, start tracking it
                    recording_state = "SILENCE_DETECTED"
                    silence_start_time = current_time
                    print("Potential pause detected - monitoring for continued silence")
            
            # STATE: Tracking silence period
            elif recording_state == "SILENCE_DETECTED":
                if not is_silent_chunk:
                    # Speech resumed, go back to recording
                    recording_state = "RECORDING"
                    print("Speech resumed - continuing recording")
                    silence_start_time = None
                else:
                    # Still silent, check duration
                    silence_duration = current_time - silence_start_time
                    # Print countdown
                    if int(silence_duration) != int(silence_duration - 0.1):  # Only print when second changes
                        print(f"Silence duration: {silence_duration:.1f}s / {silence_seconds}s", flush=True)
                    
                    # Check if we've reached the silence threshold
                    if silence_duration >= silence_seconds:
                        print(f"Silence threshold reached ({silence_seconds}s) - stopping recording")
                        break
            
            # Check for max duration
            if current_time - start_time > max_duration:
                print(f"Maximum duration of {max_duration} seconds reached")
                break
                
    except KeyboardInterrupt:
        print("\nRecording stopped by user")
    except Exception as e:
        print(f"\nRecording error: {e}")
    finally:
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        # Play a sound to indicate recording has ended
        subprocess.run(["afplay", "/System/Library/Sounds/Tink.aiff"], check=False)
        print("Recording finished")
        
        # Save the audio data to a WAV file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

def transcribe_audio(audio_file_path):
    """Transcribe audio using OpenAI's API"""
    print("Transcribing audio...")
    
    # Open the audio file
    with open(audio_file_path, "rb") as audio_file:
        # Transcribe the audio
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file
        )
    
    print("Transcription complete")
    return transcription.text

def speak_text(text, play_back=True, voice="onyx"):
    """Convert text to speech using OpenAI's TTS model"""
    if not play_back:
        print("Skipping playback")
        return
    
    print(f"Converting to speech using voice: {voice}...")
    
    # Generate temporary filename for speech
    speech_file_path = tempfile.gettempdir() + f"/tts_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    
    try:
        # Generate speech using the recommended streaming approach
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice=voice.lower(),
            input=text
        ) as response:
            # Save the response to a file
            with open(speech_file_path, 'wb') as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        
        # Play the audio
        print("Playing speech...")
        subprocess.run(["afplay", speech_file_path], check=True)
        
        # Clean up
        os.remove(speech_file_path)
        print("Speech playback complete")
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

def copy_to_clipboard(text):
    """Copy text to system clipboard"""
    pyperclip.copy(text)
    print("Copied to clipboard")

def main():
    """Main function with argument parsing"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Voice Recording and Transcription Tool")
    parser.add_argument("-s", "--silence", type=int, default=3, 
                        help="Silence threshold in seconds (default: 3)")
    parser.add_argument("-m", "--max-duration", type=int, default=60,
                        help="Maximum recording duration in seconds (default: 60)")
    parser.add_argument("-p", "--play-back", type=str, default="true",
                        help="Whether to play back the transcription (default: true)")
    parser.add_argument("-v", "--voice", type=str, default="onyx",
                        help="TTS voice to use (default: onyx, options: alloy, ash, ballad, coral, echo, fable, onyx, nova, sage, shimmer, verse)")
    
    args = parser.parse_args()
    
    # Convert play-back argument to boolean
    play_back = args.play_back.lower() in ["true", "yes", "y", "1"]
    
    # Validate voice selection
    valid_voices = ["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer", "verse"]
    voice = args.voice.lower()
    if voice not in valid_voices:
        print(f"Warning: Invalid voice '{voice}'. Using default 'onyx' instead.")
        print(f"Valid voices are: {', '.join(valid_voices)}")
        voice = "onyx"
    
    try:
        # Generate temporary filename for recording
        audio_file = tempfile.gettempdir() + f"/recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        
        # Record audio
        record_audio(audio_file, silence_seconds=args.silence, max_duration=args.max_duration)
        
        # Transcribe audio
        transcription = transcribe_audio(audio_file)
        print(f"Transcription: {transcription}")
        
        # Copy to clipboard
        copy_to_clipboard(transcription)
        
        # Speak the transcription
        speak_text(transcription, play_back, voice)
        
        # Clean up
        os.remove(audio_file)
        print("Temporary audio file removed")
        
        return transcription
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()