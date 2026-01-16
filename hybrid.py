class Content:
    def __init__(self, nomi, davomiyligi):
        self.name = nomi
        self.duration = davomiyligi

    def get_content_info(self):
        return f"Kontent nomi: {self.name}  davomiyligi: {self.duration} daqiqa"


class Video(Content):
    def __init__(self, nomi, davomiyligi, tasvir_sifati, fps):
        Content.__init__(self, nomi, davomiyligi)
        self.resolution = tasvir_sifati
        self.fps = fps

    def get_play_video(self):
        return f"'{self.name}' video fayli ({self.resolution}) sifatda va {self.fps} kadr/sekundda  ijro etilmoqda"


class Audio(Content):
    def __init__(self, nomi, davomiyligi, audio_codec):
        Content.__init__(self, nomi, davomiyligi)
        self.audio_codec = audio_codec

    def get_play_audio(self):
        return f"'{self.name}' audio fayli ({self.audio_codec}) ovoz kodekida ijro etilmoqda"


class AudioVideo(Video, Audio):
    def __init__(self, nomi, davomiyligi, tasvir_sifati, fps, audio_codec):
        Video.__init__(self, nomi,davomiyligi, tasvir_sifati, fps)
        Audio.__init__(self, nomi,davomiyligi, audio_codec)

    def get_audio_video(self):
        return f"{self.duration} daqiqalik {self.name} nomli kontent {self.resolution} sifatda va {self.audio_codec} ovoz kodekida ko'rsatilmoqda "


p = AudioVideo("Pyton asoslari", 8, "1080p","24" ,"wav" )

print(p.get_content_info())
print(p.get_play_audio())
print(p.get_play_video())
print(p.get_audio_video())
