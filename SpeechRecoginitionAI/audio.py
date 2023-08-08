import wave
import pyaudio

def play_audio(filename):
    chunk=1024
    wf=wave.open(filename,'rb')
    pa=pyaudio.PyAudioyAudio()

    stream=pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data_stream=wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream=wf.readframes(chunk)
    stream.close()
    pa.terminate()

play_audio('be-gentle-with-yourself-485.mp3')
def 