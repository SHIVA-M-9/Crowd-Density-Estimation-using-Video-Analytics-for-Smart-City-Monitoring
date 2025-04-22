import cv2
import os


def extract_frames(video_path, output_folder, frame_interval=1):
    """
    Extract frames from a video file and save them as images.

    Parameters:
        video_path (str): Path to the input video file
        output_folder (str): Folder to save extracted frames
        frame_interval (int): Extract every nth frame (1=every frame)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file")
        return

    frame_count = 0
    extracted_count = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If frame is not read correctly, break the loop
        if not ret:
            break

        # Only process frames at the specified interval
        if frame_count % frame_interval == 0:
            # Save the frame as an image file
            output_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(output_path, frame)
            extracted_count += 1

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Extracted {extracted_count} frames from {frame_count} total frames")


# Example usage
if __name__ == "__main__":
    video_file = "video2.mp4"  # Replace with your video file path
    output_dir = "extracted_frames2"  # Folder where frames will be saved

    # Extract every 10th frame (change 10 to 1 to extract all frames)
    extract_frames(video_file, output_dir, frame_interval=10)