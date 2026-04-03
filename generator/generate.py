# favicon generator py
import os
from favicons import Favicons

HTML_TEMPLATE = """<!-- Favicon Suite ({variant}) -->
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="64x64" href="/favicon-64x64.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicon-128x128.png">
<link rel="icon" type="image/png" sizes="256x256" href="/favicon-256x256.png">

<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="167x167" href="/apple-touch-icon-167x167.png">
<link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">

<link rel="manifest" href="/site.webmanifest">
<meta name="msapplication-config" content="/browserconfig.xml">
"""

MANIFEST_TEMPLATE = """{{
  "name": "Favicon Suite ({variant})",
  "short_name": "Favicon",
  "icons": [
    {{
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    }},
    {{
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }}
  ],
  "theme_color": "{color}",
  "background_color": "{color}",
  "display": "standalone"
}}
"""

BROWSERCONFIG_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
  <msapplication>
    <tile>
      <square150x150logo src="/mstile-150x150.png"/>
      <TileColor>{color}</TileColor>
    </tile>
  </msapplication>
</browserconfig>
"""


def write_html_snippet(output_dir: str, variant: str):
    path = os.path.join(output_dir, "head-snippet.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(variant=variant))
    print(f"  → wrote HTML snippet")


def write_manifest(output_dir: str, variant: str, color: str):
    path = os.path.join(output_dir, "site.webmanifest")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MANIFEST_TEMPLATE.format(variant=variant, color=color))
    print(f"  → wrote manifest")


def write_browserconfig(output_dir: str, variant: str, color: str):
    path = os.path.join(output_dir, "browserconfig.xml")
    with open(path, "w", encoding="utf-8") as f:
        f.write(BROWSERCONFIG_TEMPLATE.format(color=color))
    print(f"  → wrote browserconfig")


def generate_variant(source_path: str, output_dir: str, variant: str, color: str):
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating {variant} variant…")

    with Favicons(source_path, output_dir) as fav:
        fav.generate()

    write_html_snippet(output_dir, variant)
    write_manifest(output_dir, variant, color)
    write_browserconfig(output_dir, variant, color)

    print(f"✔ Completed {variant} variant → {output_dir}\n")


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Light
    generate_variant(
        source_path=os.path.join(root, "source", "light", "logo.png"),
        output_dir=os.path.join(root, "dist", "light"),
        variant="light",
        color="#ffffff"
    )

    # Dark
    generate_variant(
        source_path=os.path.join(root, "source", "dark", "logo.png"),
        output_dir=os.path.join(root, "dist", "dark"),
        variant="dark",
        color="#000000"
    )


if __name__ == "__main__":
    main()
