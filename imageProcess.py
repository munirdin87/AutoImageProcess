from PIL import Image
import os

def process_image(image_path, output_folder):
    try:
        image = Image.open(image_path)

        # Example: Convert the image to grayscale
        processed_image = image.convert("L")

        # Save the processed image to the output folder
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        processed_image.save(output_path)

        print(f"Processed and saved: {os.path.basename(image_path)}")

         # Delete the input image after processing
        os.remove(image_path)
        print(f"Deleted: {os.path.basename(image_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(image_path)}: {str(e)}")