import os
from PIL import Image

def process_images(input_folder, output_folder, target_width, target_height):
    """
    Processes images in a folder, padding them to 16:9 aspect ratio 
    and resizing them to the target resolution.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where processed images will be saved.
        target_width (int): Desired output width (e.g., 1600 for 1600x900).
        target_height (int): Desired output height (e.g., 900 for 1600x900).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Supported image extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    original_width, original_height = img.size

                    # Scale to fit within 16:9 target while preserving aspect ratio
                    aspect_ratio_target = target_width / target_height
                    aspect_ratio_img = original_width / original_height

                    if aspect_ratio_img > aspect_ratio_target:
                        # Image is too wide → fit to width
                        new_width = target_width
                        new_height = int(original_height * (target_width / original_width))
                    else:
                        # Image is too tall/narrow → fit to height
                        new_height = target_height
                        new_width = int(original_width * (target_height / original_height))

                    # Resize with preserved aspect ratio
                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Create new 16:9 image with white background
                    canvas = Image.new("RGB", (target_width, target_height), (255, 255, 255))

                    # Center image
                    paste_x = (target_width - new_width) // 2
                    paste_y = (target_height - new_height) // 2
                    canvas.paste(resized_img, (paste_x, paste_y))

                    # Save result
                    canvas.save(output_path)
                    print(f"Processed '{filename}' → '{output_path}'")

            except Exception as e:
                print(f"Error processing '{filename}': {e}")

if __name__ == "__main__":
    # Example: 1280x720 (HD) or 1920x1080 (Full HD)
    input_folder = "/home/thijm/Github/thijmennijdam.github.io/images/publications_original"
    output_folder = "/home/thijm/Github/thijmennijdam.github.io/images/publications"
    target_width, target_height = 1280, 720   # 16:9 aspect ratio

    print(f"Starting image processing from '{input_folder}' to '{output_folder}' at {target_width}x{target_height}...")
    process_images(input_folder, output_folder, target_width, target_height)
    print("Image processing complete.")
