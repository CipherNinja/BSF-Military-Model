import cv2
import numpy as np
from extract_roads import get_road_mask
from extract_airforce import extract_red_objects

def combine_masks_with_overlay(road_mask, iaf_mask, original_image):
    """
    Overlay road marks and IAF positions on the original image.

    Parameters:
        road_mask (numpy.ndarray): Binary mask for roads.
        iaf_mask (numpy.ndarray): Binary mask for IAF bases.
        original_image (numpy.ndarray): Original colored map image.

    Returns:
        overlay_image (numpy.ndarray): Original image with road and IAF overlays.
    """
    # Resize Road mask to match the original image
    if road_mask.shape[:2] != original_image.shape[:2]:
        print("Resizing Road mask to match dimensions of Original image.")
        road_mask = cv2.resize(road_mask, (original_image.shape[1], original_image.shape[0]))

    # Resize IAF mask to match Original image if necessary
    if iaf_mask.shape[:2] != original_image.shape[:2]:
        print("Resizing IAF mask to match dimensions of Original image.")
        iaf_mask = cv2.resize(iaf_mask, (original_image.shape[1], original_image.shape[0]))

    # Convert IAF mask to binary single-channel
    iaf_mask_gray = cv2.cvtColor(iaf_mask, cv2.COLOR_BGR2GRAY)
    _, iaf_mask_binary = cv2.threshold(iaf_mask_gray, 1, 255, cv2.THRESH_BINARY)

    # Ensure both masks are of type uint8
    road_mask = road_mask.astype(np.uint8)
    iaf_mask_binary = iaf_mask_binary.astype(np.uint8)

    # Overlay road marks (black color) onto the original image
    roads_overlay = np.zeros_like(original_image)
    roads_overlay[road_mask > 0] = [0, 0, 0]  # Black color for roads
    overlay_image = cv2.addWeighted(original_image, 1, roads_overlay, 0.5, 0)

    # Annotate IAF positions (circles for IAF bases)
    contours, _ = cv2.findContours(iaf_mask_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Calculate the center and radius for a circle around each IAF base
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw grey circle
        cv2.circle(overlay_image, center, radius, (128, 128, 128), -1)  # Grey color (BGR)

    return overlay_image

if __name__ == "__main__":
    # Paths to the input images
    road_image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\resource\maps\roads_and_rivers.png"
    iaf_image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\resource\maps\iaf_map.png"
    original_image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\resource\maps\original_map.png"

    # Generate road mask
    road_mask = get_road_mask(road_image_path)

    # Load IAF image and original map image
    iaf_image = cv2.imread(iaf_image_path)
    original_image = cv2.imread(original_image_path)

    if iaf_image is None or original_image is None:
        raise FileNotFoundError("Failed to load input images.")

    # Extract IAF mask
    iaf_mask = extract_red_objects(iaf_image)

    # Combine masks and overlay on the original image
    overlay_image = combine_masks_with_overlay(road_mask, iaf_mask, original_image)

    # Resize final image for better visualization
    overlay_image_resized = cv2.resize(overlay_image, (800, 600))  # Resize to fit your screen

    # Display the final overlay
    cv2.imshow("Final Overlay (Roads + IAF)", overlay_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the final overlay image (optional)
    final_image_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\Data\output\final_overlay.png"
    cv2.imwrite(final_image_path, overlay_image_resized)
