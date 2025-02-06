import cv2
import detecttext
import util
import chromesearch

def process_video():
    # Set the source
    source = 0  # Uncomment this to use the webcam
    # source = "./input/test2.mp4"  # Path to the video file

    # Capture the video
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Unable to open the video source.")
        return

    # Loop to read and display video frames
    while True:
        ret, frame = cap.read()  # Read a frame from the video source
        title=""
        author=""
        publisher=""
        other=""
        combined_text = ""  # Initialize the search text
        if not ret:
            print("End of video or error reading the frame.")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
        if cv2.waitKey(1) & 0xFF == ord('c'):
            result = detecttext.detect_text(frame)  # Detect text in the frame
            image = frame.copy()
            title, author, publisher, other, combined_text = detecttext.show_textregion(image, result)  # Show the text region in the frame
            # title = util.get_longest_word(searchtext)
            # Combine title, author, and publisher (and any other info)
            search_query = f"{title}"
            chromesearch.google_search(search_query)  # Search the text in Google

        # Display the frame in a window
        cv2.imshow("Video Frame", frame)

        # Exit on pressing the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close display windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function
process_video()
