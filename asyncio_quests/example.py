import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages
import sys
from tkinter import Tk
from tkinter import filedialog
import os


def convert_images_to_pdf(input_paths, output_path):
    with PdfPages(output_path) as pdf:
        for input_path in input_paths:
            # Load the image
            img = mpimg.imread(input_path)

            # Create a figure and axis
            fig, ax = plt.subplots(
                figsize=(img.shape[1] / 100, img.shape[0] / 100))  # Adjust size based on image dimensions

            # Display the image
            ax.imshow(img)
            ax.axis('off')  # Hide axes

            # Save the current figure to the PDF
            pdf.savefig(fig, bbox_inches='tight', pad_inches=0, dpi=100)
            plt.close(fig)  # Close the figure to free memory


if __name__ == "__main__":
    # Create a root window and hide it
    root = Tk()
    root.withdraw()

    # Open file dialog to select input JPG files (allows multiple)
    input_paths = filedialog.askopenfilenames(
        title="Select JPG file(s) to convert",
        filetypes=[("JPG files", "*.jpg;*.jpeg")]
    )

    if not input_paths:
        print("No input file(s) selected. Exiting.")
        sys.exit(1)

    # If only one file selected, derive output path in the same directory
    if len(input_paths) == 1:
        output_path = os.path.splitext(input_paths[0])[0] + ".pdf"
    else:
        # For multiple files, use the directory of the first file and a default name
        first_dir = os.path.dirname(input_paths[0])
        output_path = os.path.join(first_dir, "combined.pdf")

    # Convert the image(s) to PDF
    convert_images_to_pdf(input_paths, output_path)
    print(f"Converted {len(input_paths)} file(s) to {output_path}")