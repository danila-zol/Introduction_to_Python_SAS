from pydub.playback import play
from pydub.generators import Sine, Sawtooth

# Create two generators of different shapes
generator1 = Sawtooth(400)
generator2 = Sine(100)

# Use each generator to synthesize a sound for 2 seconds (2000ms)
tone1 = generator1.to_audio_segment(duration=2000)
tone2 = generator2.to_audio_segment(duration=2000)


# play(tone1.low_pass_filter(14000).apply_gain(-15))
# quit()

# Play them both! (careful: overlays tend to get loud!)
play(
    tone1.overlay(tone2) \
        .apply_gain(-30) \
)
