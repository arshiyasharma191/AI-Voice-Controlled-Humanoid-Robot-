import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


def record_audio(filename="input.wav", fs=16000, silence_threshold=0.01, silence_duration=1.5):
    print(" Listening... (speak now)")

    recording = []
    silence_counter = 0

    def callback(indata, frames, time, status):
        nonlocal silence_counter

        volume_norm = np.linalg.norm(indata) / frames
        recording.append(indata.copy())

        # Detect silence
        if volume_norm < silence_threshold:
            silence_counter += 1
        else:
            silence_counter = 0

        # Stop if silence lasts long enough
        if silence_counter > silence_duration * fs / frames:
            raise sd.CallbackStop()

    try:
        with sd.InputStream(samplerate=fs, channels=1, callback=callback):
            sd.sleep(10000)  # max wait, stops early if silence detected

    except sd.CallbackStop:
        pass

    audio = np.concatenate(recording, axis=0)

    # Normalize and save
    audio = np.squeeze(audio)
    audio = (audio * 32767).astype(np.int16)

    wav.write(filename, fs, audio)

    print("Saved:", filename)
    return filename