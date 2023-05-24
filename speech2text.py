import glob
from pydub import AudioSegment # uses FFMPEG
import speech_recognition as sr
import subprocess

def creat_audiofiles():
    
    split_audiofiles = [f.split('.')[0] for f in glob.glob('*/*.mp3', recursive=True)]#find all mp3 files, to avoid double processing of videofiles
    videofiles = [f for f in glob.glob('*/*.mp4', recursive=True) if f.split('.')[0] not in split_audiofiles]  +[f for f in glob.glob('*/*.m4v', recursive=True) if f.split('.')[0] not in split_audiofiles] #only turn mp4 and m4v into mp3 if it doesn't exist yet


    print(f'de volgende bestanden worden tot mp3 verwerkt: {videofiles}')

    for file in videofiles:
        subprocess.run(f"ffmpeg -i {file} {file.split('.')[0] + '.mp3'}",shell=True)
def get_audiofiles():

    split_txt_files = [f.split('.')[0] for f in glob.glob('*/*.txt', recursive=True)] #find all text files, to avoid double processing of textfiles
    audiofiles = [f for f in glob.glob('*/*.mp3', recursive=True) if f.split('.')[0] not in split_txt_files]
    print(f'de volgende bestanden worden verwerkt tot txt-bestand: {audiofiles}')
    return audiofiles

def process(filepath, chunksize=60000):
    #0: load mp3
    sound = AudioSegment.from_mp3(filepath)

    #1: split file into 60s chunks
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
    chunks = list(divide_chunks(sound, chunksize))

    r = sr.Recognizer()
    #2: per chunk, save to wav, then read and run through recognize_google() (recognize_google only works for .wav files)
    string_index = {}
    for index,chunk in enumerate(chunks):
        temp = 'temp.wav'
        chunk.export(temp, format='wav')
        with sr.AudioFile(temp) as source:
            audio = r.record(source)
        s = r.recognize_google(audio, language="NL-nl")
        string_index[index] = s
        break
    return ' '.join([string_index[i] for i in range(len(string_index))])
def main():
    creat_audiofiles()
    audiofiles= get_audiofiles()
    for audio_file_name in audiofiles:
        text = process(audio_file_name)
        output_file = audio_file_name.split('.')[0] + '.txt'
        print(f'bestand {audio_file_name} verwerkt') 
        with open(output_file, 'w') as file:
            file.write(text)
if __name__ == '__main__':
    main()