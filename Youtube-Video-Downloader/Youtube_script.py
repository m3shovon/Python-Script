from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=au-Oixsfpmk')
streams = yt.streams

# Print available streams
print(streams.all())

# Filter streams based on criteria (file extension and progressive)
filtered_streams = streams.filter(file_extension="mp4", progressive=True)

# Print filtered streams
print(filtered_streams.all())

# Get the stream with itag 22 (assuming it's available in the filtered streams)
stream = filtered_streams.get_by_itag(22)

# Download the stream
if stream:
    stream.download()
    print("======== Download successful! ========")
else:
    print("======== Stream not found ========")
