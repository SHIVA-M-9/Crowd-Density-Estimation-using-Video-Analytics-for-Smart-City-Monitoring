import os
import cv2


def count_faces(img_path):
    # print("Processing image:", img_path)
    try:
        # Load the image
        image = cv2.imread(img_path)

        # Check if image was loaded successfully
        if image is None:
            print(f"Failed to load image at: {img_path}")
            return

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load Haar cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        print('Faces Detected:', len(faces))


        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 8)

        # Display the output image
        cv2.imshow("Detected Faces", image)
        cv2.waitKey(100)  # Display for 100ms before moving to next image
        # cv2.destroyAllWindows()  # Don't destroy window between images for smoother viewing
        return len(faces)

    except Exception as e:
        print(f"Error occurred while processing {img_path}: {e}")


def process_images_in_folder(folder_path):
    """
    Loop through all image files in a folder and process each one
    """
    # Supported image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']

    # Create a window for display
    cv2.namedWindow("Detected Faces", cv2.WINDOW_NORMAL)
    people = 0

    # Get all files in the directory
    for filename in sorted(os.listdir(folder_path)):

        # Check if the file is an image
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            # Full path to the image
            image_path = os.path.join(folder_path, filename)
            people+=count_faces(image_path)

    # Close the window when done
    print("people",people)
    if(people<10):
        print("low crord")
    elif(people<25):
        print("avg crord")
    else:
        print("large crord")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Specify your folder containing images
    images_folder = "C:/Users/Shiva M/PycharmProjects/PythonProject/extracted_frames2"

    # Verify folder exists
    if not os.path.exists(images_folder):
        print(f"Error: Folder does not exist: {images_folder}")
    else:
        print(f"Processing images from: {images_folder}")
        process_images_in_folder(images_folder)