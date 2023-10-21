# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Window name in which image is displayed
    window_name = 'Image'

    # Using cv2.flip() method
    # Use Flip code 0 to flip vertically
    image = cv2.flip(frame, 1)

    # Display the resulting frame
    # cv2.imshow('frame', window_name)
    # Displaying the image
    cv2.imshow(window_name, image)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
