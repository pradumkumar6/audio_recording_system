import pyaudio
import wave
from array import array
from struct import pack
def playfile(file):
  CHUNK = 1024
  wf = wave.open(file,'rb')
  
  p = pyaudio.PyAudio()
  # To record or play audio , open a stream on the desired devics
  stream = p.open(
    format= p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True
  )
  data = wf.readframes(CHUNK)
  while len(data)>0:
    stream.write(data)
    data = wf.readframes(CHUNK)
    
  stream.stop_stream()
  stream.close()
  p.terminate()
  
  
playfile("output1.wav")