#########################
# Imports:
import wave
import matplotlib as plt
import numpy as np

# Constants:
#########################

def plotWave(file_name: str, start: int, incroment: int, dir='data/audio/'):

    full_path = dir + file_name
    obj = wave.open(full_path ,'rb')

    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(-1)
    obj.close()

    t_audio_ms = (n_samples/sample_freq)*1000

    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    times = np.linspace(0, t_audio_ms, num=n_samples)

    plt.figure.Figure()
    plt.pyplot.plot(times, signal_array)
    plt.pyplot.title(file_name[:-4])
    plt.pyplot.ylabel('Signal Wave')
    plt.pyplot.xlabel('Time (ms)')
    plt.pyplot.xlim(0, t_audio_ms)

    # Adding veritcal Lines
    plt.pyplot.axvline(x=start, color='y') # Starting point
    for i in range(50):
        plt.pyplot.axvline(x=(start+((i+1)*incroment)), color='r') # Incroment

    plt.pyplot.show()