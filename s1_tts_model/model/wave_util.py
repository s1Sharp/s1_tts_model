import contextlib
import wave
import io

def audio_as_int16(audio):
    return (audio * 32767).numpy().astype('int16')


# TODO:: impl class writer, s3 for example
def write_bytes(bytesio_object: io.BytesIO, filepath: str, rwflag = "wb"):
    with open(filepath, rwflag) as f:
        f.write(bytesio_object.getbuffer())

def write_wave(path, audio, sample_rate):
    """
    Writes a .wav file.
    Takes path, PCM audio data, and sample rate.
    """
    with contextlib.closing(wave.open(path, 'wb')) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio)

def buff_wave(audio, sample_rate):
    """
    return io.BytesIO buffer
    Takes PCM audio data, and sample rate.
    """
    bytes_arr = io.BytesIO()
    with contextlib.closing(wave.open(bytes_arr, 'wb')) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio)
    return bytes_arr

def write_wave_as_int16(path, audio, sample_rate):
    return write_wave(path=path, audio=audio_as_int16(audio), sample_rate=sample_rate)

def buf_wave_as_int16(audio, sample_rate):
    return buff_wave(audio=audio_as_int16(audio), sample_rate=sample_rate)


# import StringIO
# import io

# buffer = StringIO.StringIO()
# audio_out = wave.open(buffer, 'w')
# audio_out.setframerate(m.getRate())
# audio_out.setsampwidth(2)
# audio_out.setcomptype('NONE', 'not compressed')
# audio_out.setnchannels(1)

# audio_out.writeframes(raw_audio)
# audio_out.close()
# buffer.flush()

# # these lines do not work...
# # buffer.output(wav_buffer)
# # file = wave.open(buffer, 'r')

# # this file plays out fine in VLC
# file = open(FILE_NAME + ".wav", 'w')
# file.write(buffer.getvalue())
# file.close()
# buffer.close()