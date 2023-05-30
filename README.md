# ReadMe - YouTube Video Downloader

This code is a simple YouTube video downloader written in Python using the `pytube` library. It allows you to download a YouTube video by providing the video URL.

## Prerequisites
Before running the code, make sure you have the following dependencies installed:
- `pytube`: You can install it using `pip install pytube`.
- `tqdm`: You can install it using `pip install tqdm`.

## How to Use
1. Run the Python script.
2. You will be prompted to paste the YouTube video link.
3. Enter the video link and press Enter.
4. The script will print the title and thumbnail URL of the video and start the download process.
5. A progress bar will be displayed to show the download progress.
6. Once the download is complete, the script will print "DOWNLOAD COMPLETE!!!"

## Code Explanation
1. Import the necessary libraries:
    - `pytube`: Used to interact with the YouTube video.
    - `tqdm`: Used to display the progress bar.

2. Set the `total_length` variable to the desired number of iterations for the progress bar.

3. Create a `tqdm` progress bar object with a total length equal to `total_length` and a unit of 'iteration'.

4. Prompt the user to enter the YouTube video link using the `input()` function and store it in the `link` variable.

5. Create a `pytube.YouTube` object by passing the `link` variable to it.

6. Print the title and thumbnail URL of the video using the `title` and `thumbnail_url` attributes of the `YouTube` object.

7. Print a message indicating that the download has started.

8. Use a for loop to iterate `total_length` times. Inside the loop:
    - Get the stream with the highest resolution using `my_video.streams.get_highest_resolution()`.
    - Download the stream and save it in the current directory using `stream.download(".")`.
    - Pause for a short time using `time.sleep(0.1)` to avoid overwhelming the server.
    - Update the progress bar by calling `progress_bar.update(1)`.

9. Close the progress bar using `progress_bar.close()`.

10. Print a message indicating that the download is complete.

## Note
- Make sure you have proper permissions to download the YouTube video before using this code.
- Keep in mind any copyright restrictions and use this code responsibly.
- Some videos may not be available for download due to restrictions imposed by the uploader or YouTube.

