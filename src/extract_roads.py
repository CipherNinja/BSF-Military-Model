import cv2
import numpy as np

def get_road_mask(image_path):
    """
    Generate a cleaned mask for roads (red/maroon) from an input map image.

    Parameters:
        image_path (str): The file path to the input image.

    Returns:
        mask_red_cleaned (numpy.ndarray): The cleaned binary mask for roads.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Resize the image (optional, for convenience)
    image = cv2.resize(image, (800, 600))  # Adjust dimensions as needed

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the HSV range for red and maroon (roads)
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for both red ranges
    mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

    # Combine the two red masks
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Clean up the mask using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask_red_cleaned = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)

    return mask_red_cleaned

if __name__ == "__main__":
    # File path to the image
    image_path = r'C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\resource\maps\roads_and_rivers.png'

    # Generate the mask
    mask = get_road_mask(image_path)

    # Load the original image
    image = cv2.imread(image_path)

    # Ensure the mask matches the image size
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))

    # Convert the mask to uint8
    mask = mask.astype(np.uint8)

    # Apply the mask to highlight roads
    highlighted_roads = cv2.bitwise_and(image, image, mask=mask)

    # Display the results
    # Resize the output image to a smaller size for display
    scaled_highlighted_roads = cv2.resize(highlighted_roads, (600, 400))  # Adjust to your desired size

    # Display the resized output image
    cv2.imshow("Highlighted Roads (Scaled)", scaled_highlighted_roads)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
