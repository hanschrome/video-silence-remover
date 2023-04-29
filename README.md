# Video Silence Remover

This Python application removes silent parts from a video using a specified threshold. It accepts input video files in various formats, such as MP4 and MOV.

## Requirements

- Docker
- Docker Compose
- Make (optional)

## Project Structure

[.
├── data
│   └── input.mp4
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── main.py
└── requirements.txt]

## Setup

1. Clone this repository:

   [cd video-silence-remover]

2. Place your input video file in the `data` folder.

## Usage

### With Makefile

1. Build the Docker container:

   [make build]

2. Edit the video file by removing silent parts:

   [make edit input=input.MOV output=output.MOV]

Replace `input.MOV` and `output.MOV` with the desired input and output video file names.

3. Clean up Docker resources:

   [make clean]

### Without Makefile

1. Build the Docker container:

   [docker-compose build]

2. Edit the video file by removing silent parts:

   [docker-compose run --rm video-editor input.MOV output.MOV]

Replace `input.MOV` and `output.MOV` with the desired input and output video file names.

3. Clean up Docker resources:

   [docker-compose down]

## Customization

To customize the audio threshold and minimum silence length, you can modify the `remove_silence` function parameters in `main.py`:

[def remove_silence(input_file, output_file, threshold=-40, min_silence_length=1000):]

- `threshold`: The silence threshold in dBFS. Adjust this value to consider audio segments as silent or non-silent.
- `min_silence_length`: The minimum length of silence in milliseconds. Segments shorter than this will not be considered as silent.

## License

This project is licensed under the [MIT License](LICENSE).

