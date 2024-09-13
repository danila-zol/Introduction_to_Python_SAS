from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

test_audio = AudioSegment.from_file("./src/test_in.mp3")
test_audio += AudioSegment.silent(300)
test_audio += Sine(200).to_audio_segment(300).apply_gain(-4)

play(test_audio)

test_audio.export("./test_out.mp3", format="mp3")