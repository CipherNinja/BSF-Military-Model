import cv2
import numpy as np

def extract_and_focus_airplane_symbols(image_path):
    """
    Extract and isolate airplane symbols (red and white) while masking the rest of the map as black.

    Parameters:
        image_path (str): File path to the map image.

    Returns:
        focused_image (numpy.ndarray): The image showing only airplane symbols with the map blacked out.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Resize image (optional)
    image = cv2.resize(image, (800, 600))

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red
    mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Define color range for white
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

    # Combine the red and white masks
    mask_combined = cv2.bitwise_or(mask_red, mask_white)

    # Apply the mask to isolate airplane symbols
    focused_image = cv2.bitwise_and(image, image, mask=mask_combined)

    # Make the rest of the map black (unfocused)
    black_background = np.zeros_like(image)  # Create a black image
    focused_image_with_black = np.where(mask_combined[..., None] > 0, focused_image, black_background)

    return focused_image_with_black



def extract_red_objects(image):
    """
    Extract only the red objects from an image and black out all other colors.

    Parameters:
        image (numpy.ndarray): Input image.

    Returns:
        red_objects (numpy.ndarray): Image showing only red objects.
    """
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for both red ranges
    mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

    # Combine the two red masks
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Apply the red mask to the image
    red_objects = cv2.bitwise_and(image, image, mask=mask_red)

    return red_objects

if __name__ == "__main__":
    # Path to the map image
    image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\resource\maps\iaf_map.png"

    # Extract and focus airplane symbols (previous step)
    output_image = extract_and_focus_airplane_symbols(image_path)

    # Extract only red objects from the output
    red_only_image = extract_red_objects(output_image)

    # Display the result
    cv2.imshow("Red Objects Only", red_only_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
