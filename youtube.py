import pytube
from tqdm import tqdm
import time
from colorama import Fore, Back, Style

total_length = 100

progress_bar = tqdm(total = total_length, unit = 'iteration')


link = str(input(Fore.GREEN + "[=>] Paste Your Link Here: "))
print('\n')

my_video = pytube.YouTube(link)
print(Fore.BLUE+f"[+]	VIDEO TITLE: {my_video.title}")
print(Fore.BLUE+f"[+]	THUMBNAIL: {my_video.thumbnail_url} \n")
print(Style.BRIGHT + "[+] THE DOWNLOAD HAS STARTED... \n\n")

for i in range(total_length):
	stream = my_video.streams.get_highest_resolution()
	stream.download(".")
	time.sleep(0.1)
	progress_bar.update(1)
	
progress_bar.close()

print("\n [<+>]	DOWNLOAD COMPLETE!!!")
