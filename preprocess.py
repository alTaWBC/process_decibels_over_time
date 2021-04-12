import threading
import os
from pydub import AudioSegment, effects



input_location = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time\audios"
temporary_location = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time\ffmpeg_converted"
output_location = r"C:\Users\WilliamCosta\Desktop\tese_repositories\process_decibels_over_time\normalized"
conversion_line = "ffmpeg -i {0} -ac 1 -ar 44100 -f wav {1}"

files = [f for f in os.listdir(input_location)]

print(len(files))
threads = 8


def converFile(filename):
    origin = os.path.join(input_location, filename)
    temporary = os.path.join(temporary_location, filename)
    destination = os.path.join(output_location, filename)

    # Convert to 16bits mono 44100Hz
    os.system(conversion_line.format(origin, temporary))
    
    #Normalize
    rawsound = AudioSegment.from_file(temporary, "wav")
    normalizedsound = effects.normalize(rawsound)
    normalizedsound.export(destination, format="wav")




for i in range(0, len(files)+1, threads):
    thread_pool = []
    for j in range(threads):
        if i + j >= len(files):
            break
        filename = files[i+j]
        thread = threading.Thread(target=converFile, args=(filename,))
        thread_pool.append(thread)
        thread.start()
    print(f"Threads {i} to {i+j} started")
    for thread in thread_pool:
        thread.join()
        
    print(f"Threads {i} to {i+j} ended")
