from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play

kick1 = AudioSegment.from_mp3("./src/drumloop/kick1.mp3").apply_gain(-8)
kick2 = AudioSegment.from_mp3("./src/drumloop/kick2.mp3").apply_gain(-8)
kick3 = AudioSegment.from_mp3("./src/drumloop/kick3.mp3").apply_gain(-8)


# Returns a list of nonsilent segments
kick1 = split_on_silence(kick1, min_silence_len=10, silence_thresh=-32)[0]

# Alternatively return a whole segment with removed silence
kick2 = kick2.strip_silence(silence_thresh=-32)

# You can always eyeball it anyways :D
kick3 = kick3[:600]


### Making a drum loop

kick1 = kick1.apply_gain(-8)

kick2 = kick2 \
    .apply_gain(3) \
    .reverse() \
    .speedup(2)



drumloop = kick3 + \
            AudioSegment.silent(100) + \
            kick2*3 + \
            AudioSegment.silent(200) + \
            kick1 + \
            AudioSegment.silent(100) + \
            kick2*3 + \
            AudioSegment.silent(500)

for i in range(3):
    play(drumloop)

drumloop.export("./src/drumloop/diy_drumloop.mp3", format="mp3")
