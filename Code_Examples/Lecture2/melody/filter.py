from pydub import AudioSegment
from pydub.generators import Triangle
from pydub.playback import play

sound = Triangle(200).to_audio_segment(1000) \
                        .apply_gain(-12)

# No filter
play(sound + AudioSegment.silent())

# Volume
play(sound.low_pass_filter(5000) + AudioSegment.silent())

# Texture
play(sound.high_pass_filter(5000) + AudioSegment.silent())
