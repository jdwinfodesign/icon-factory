# favicon generator py
import os
from favicons import Favicons

def generate_variant(source_path: str, output_dir: str):
    """
    Generate a full favicon suite from a single source image.

    source_path: path to the master PNG or SVG (2048px recommended)
    output_dir: directory where the favicon suite will be written
    """

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate the full suite
    with Favicons(source_path, output_dir) as fav:
        fav.generate()

    print(f"Generated favicon suite → {output_dir}")


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Light variant
    light_source = os.path.join(root, "source", "light", "logo.png")
    light_output = os.path.join(root, "dist", "light")
    generate_variant(light_source, light_output)

    # Dark variant
    dark_source = os.path.join(root, "source", "dark", "logo.png")
    dark_output = os.path.join(root, "dist", "dark")
    generate_variant(dark_source, dark_output)


if __name__ == "__main__":
    main()
