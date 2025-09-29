# Import the necessary modules
import ffmpeg

# Define the input and output files
input_file = "H:\raeub\Music\Musik\Bea Miller - feel something (official video).mp3"
output_file = "./output.mp3"

# Define the audio filter
filter = "lowpass=f=300:d=0.1"

# Amplify the low frequencies of the input file
(
    ffmpeg
    .input(input_file)
    .filter(filter)
    .output(output_file, acodec="copy")
    .overwrite_output()
    .run()
)
