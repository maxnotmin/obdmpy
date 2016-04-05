import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

AUDIO_FOLDER = os.path.join(APP_ROOT, 'static/audio')


# print(all_audio)


def make_audio():
    all_audio = os.listdir(AUDIO_FOLDER)
    audio_list = []
    for i in all_audio:
        if i == '.DS_Store':
            pass
        else:
            audio_list.append(i)
    return sorted(audio_list)


make_audio()
