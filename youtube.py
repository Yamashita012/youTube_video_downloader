import pytube
from tqdm import tqdm
import time

total_length = 100

progress_bar = tqdm(total = total_length, unit = 'iteration')


link = str(input("[=>] Paste Your Link Here: "))

my_video = pytube.YouTube(link)
print(my_video.title)
print(my_video.thumbnail_url)
print("THE DOWNLOAD HAS STARTED...")

for i in range(total_length):
	stream = my_video.streams.get_highest_resolution()
	stream.download(".")
	time.sleep(0.1)
	progress_bar.update(1)
	
progress_bar.close()

print("DOWNLOAD COMPLETE!!!")
