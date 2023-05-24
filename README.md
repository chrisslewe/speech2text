# speech2text

To run, simply run 
```
python speech2text.py
```

In a folder where the subdirectories contain either mp3 or mp4 files, following this structure:

- speech2text
  speech2text.py
  - some_folder_name
    file.mp3
    some_other_file.mp3
    some_video_file.mp4
  - other_folder_name
    file.mp3
    
run speech2text from the main_folder within the terminal. Glob.glob is used to automatically find all speech and video-files.
Apart from the dependicies in requirements.txt, it is necessary to install FFmpeg to convert the files to the .mp3 and .wav format for processing to text. FFmpeg can be installed here: https://ffmpeg.org/download.html

To install the python dependencies, run the following command in the speech2text folder

```
pip install -r requirements.txt
```

    
