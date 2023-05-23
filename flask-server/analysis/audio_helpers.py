#########################
# Imports:
import pyaudio
import wave
import webrtcvad as VAD
import audioop
from pydub import AudioSegment

# Constants:
#########################

def waveVAD(file_name: str, dir='data/audio/'):
    full_path = dir + file_name
    # Set up PyAudio
    pa = pyaudio.PyAudio()

    # Open the .wav file
    wf = wave.open(full_path, "rb")
    print(wf.getframerate())

    # Set up the VAD algorithm
    vad = VAD.Vad()
    vad.set_mode(3)  # Aggressiveness (0-3)

    # Read the .wav file in chunks
    chunk_size = 320  # 320 => 20 ms
    while True:
        data = wf.readframes(chunk_size)
        if len(data) == 0:
            break

        # Convert the audio data to a format that VAD can process
        pcm_data, _ = audioop.ratecv(data, 2, 1, wf.getframerate(), 16000, None)

        # Detect speech using VAD
        is_speech = vad.is_speech(pcm_data, sample_rate=16000)

        # Do something with the speech detection result
        if is_speech:
            print("Speech detected")
        else:
            print("No speech detected")

