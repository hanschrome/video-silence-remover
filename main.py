import sys
from moviepy.editor import *
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def remove_silence(input_file, output_file, threshold=-40, min_silence_length=1000, padding=0.5):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile("temp_audio.wav")

    audio_segment = AudioSegment.from_wav("temp_audio.wav")
    nonsilent_slices = detect_nonsilent(audio_segment, min_silence_len=min_silence_length, silence_thresh=threshold)

    final_clips = []
    for start, end in nonsilent_slices:
        start /= 1000  # Convertir a segundos
        end /= 1000  # Convertir a segundos
        end += padding
        clip = video.subclip(start, min(end, video.duration))  
        final_clips.append(clip)

    final_video = concatenate_videoclips(final_clips)
    final_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # Eliminar el archivo de audio temporal
    os.remove("temp_audio.wav")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py input.mp4 output.mp4")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_silence(input_file, output_file)

