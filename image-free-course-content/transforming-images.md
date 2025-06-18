## Transforming Images

### Image Processing with PIL (Pillow)

[[Image description: Here's alt text describing the image:

"A graphic depicting image manipulation using Python's Pillow library.  The background is a muted grayish-blue with a semi-transparent overlay of the Python logo in shades of yellow and blue.  The text 'Python' is displayed in large, bold, white font at the top.  A thin white line separates 'Python' from the text below. Underneath, 'Pillow' is written in smaller, bold white font, followed by 'Image Manipulation' in the same style and size. The overall color scheme is dark and subdued, with the white text providing strong contrast."]](https://youtu.be/6Qs3wObeWwc)

[Pillow](https://python-pillow.org/) is Python's leading library for image processing, offering powerful tools for editing, analyzing, and generating images. It handles various formats (PNG, JPEG, GIF, etc.) and provides operations from basic resizing to complex filters.

Here's a minimal example showing common operations:

```python
# /// script
# requires-python = "&gt;=3.11"
# dependencies = ["Pillow"]
# ///

from PIL import Image, ImageEnhance, ImageFilter

async def process_image(path: str) -&gt; Image.Image:
    """Process an image with basic enhancements."""
    with Image.open(path) as img:
        # Convert to RGB to ensure compatibility
        img = img.convert('RGB')

        # Resize maintaining aspect ratio
        img.thumbnail((800, 800))

        # Apply enhancements
        img = (ImageEnhance.Contrast(img)
               .enhance(1.2))

        return img.filter(ImageFilter.SHARPEN)

if __name__ == "__main__":
    import asyncio
    img = asyncio.run(process_image("input.jpg"))
    img.save("output.jpg", quality=85)
```

Key features and techniques you'll learn:

- **Image Loading and Saving**: Handle various formats with automatic conversion
- **Basic Operations**: Resize, rotate, crop, and flip images
- **Color Manipulation**: Adjust brightness, contrast, and color balance
- **Filters and Effects**: Apply blur, sharpen, and other visual effects
- **Drawing**: Add text, shapes, and overlays to images
- **Batch Processing**: Handle multiple images efficiently
- **Memory Management**: Process large images without memory issues

### Basic Image Operations

Common operations for resizing, cropping, and rotating images:

```python
from PIL import Image

async def transform_image(
    path: str,
    size: tuple[int, int],
    rotation: float = 0
) -&gt; Image.Image:
    """Transform image with basic operations."""
    with Image.open(path) as img:
        # Resize with anti-aliasing
        img = img.resize(size, Image.LANCZOS)

        # Rotate around center
        if rotation:
            img = img.rotate(rotation, expand=True)

        # Auto-crop empty edges
        img = img.crop(img.getbbox())

        return img
```

### Color and Enhancement

Adjust image appearance with built-in enhancement tools:

```python
from PIL import ImageEnhance, ImageOps

async def enhance_image(
    img: Image.Image,
    brightness: float = 1.0,
    contrast: float = 1.0,
    saturation: float = 1.0
) -&gt; Image.Image:
    """Apply color enhancements to image."""
    enhancers = [
        (ImageEnhance.Brightness, brightness),
        (ImageEnhance.Contrast, contrast),
        (ImageEnhance.Color, saturation)
    ]

    for Enhancer, factor in enhancers:
        if factor != 1.0:
            img = Enhancer(img).enhance(factor)

    return img
```

### Filters and Effects

Apply visual effects and filters to images:

```python
from PIL import ImageFilter

def apply_effects(img: Image.Image) -&gt; Image.Image:
    """Apply various filters and effects."""
    effects = {
        'blur': ImageFilter.GaussianBlur(radius=2),
        'sharpen': ImageFilter.SHARPEN,
        'edge': ImageFilter.FIND_EDGES,
        'emboss': ImageFilter.EMBOSS
    }

    return {name: img.filter(effect)
            for name, effect in effects.items()}
```

### Drawing and Text

Add text, shapes, and overlays to images:

```python
from PIL import Image, ImageDraw, ImageFont

async def add_watermark(
    img: Image.Image,
    text: str,
    font_size: int = 30
) -&gt; Image.Image:
    """Add text watermark to image."""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Position text at bottom-right
    x = img.width - text_width - 10
    y = img.height - text_height - 10

    # Add text with shadow
    draw.text((x+2, y+2), text, font=font, fill='black')
    draw.text((x, y), text, font=font, fill='white')

    return img
```

### Memory-Efficient Processing

Handle large images without loading them entirely into memory:

```python
from PIL import Image
import os

async def process_large_images(
    input_dir: str,
    output_dir: str,
    max_size: tuple[int, int]
) -&gt; None:
    """Process multiple large images efficiently."""
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        with Image.open(input_path) as img:
            # Process in chunks using thumbnail
            img.thumbnail(max_size)
            img.save(output_path, optimize=True)
```

Practice with these resources:

- [Pillow Documentation](https://pillow.readthedocs.io/): Complete API reference
- [Python Image Processing Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/): In-depth guide
- [Sample Images Dataset](https://www.kaggle.com/datasets/lamsimon/celebs): Test images for practice

Watch these tutorials for hands-on demonstrations:

[[Image description: Here's alt text describing the image:

"A teal-colored background with subtle horizontal lines features the text 'PYTHON' in bold, golden-yellow uppercase letters.  Below it, 'IMAGE PROCESSING' is written in bold, uppercase, orange letters. The overall style suggests a title or heading related to programming and image manipulation using Python."]](https://youtu.be/dkp4wUhCwR4)

### Image Processing with ImageMagick

[ImageMagick](https://imagemagick.org/) is a powerful command-line tool for image manipulation, offering features beyond what's possible with Python libraries. It's particularly useful for:

- Batch processing large image collections
- Complex image transformations
- High-quality format conversion
- Creating image thumbnails
- Adding text and watermarks

Basic Operations:

```bash
# Format conversion
convert input.png output.jpg

# Resize image (maintains aspect ratio)
convert input.jpg -resize 800x600 output.jpg

# Compress image quality
convert input.jpg -quality 85 output.jpg

# Rotate image
convert input.jpg -rotate 90 output.jpg
```

Common Data Science Tasks:

```bash
# Create thumbnails for dataset preview
convert input.jpg -thumbnail 200x200^ -gravity center -extent 200x200 thumb.jpg

# Normalize image for ML training
convert input.jpg -normalize -strip output.jpg

# Extract dominant colors
convert input.jpg -colors 5 -unique-colors txt:

# Generate image statistics
identify -verbose input.jpg | grep -E "Mean|Standard|Kurtosis"
```

Batch Processing:

```bash
# Convert all images in a directory
mogrify -format jpg *.png

# Resize multiple images
mogrify -resize 800x600 -path output/ *.jpg

# Add watermark to images
for f in *.jpg; do
    convert "$f" -gravity southeast -draw "text 10,10 'Copyright'" "watermarked/$f"
done
```

Advanced Features:

```bash
# Apply image effects
convert input.jpg -blur 0x3 blurred.jpg
convert input.jpg -sharpen 0x3 sharp.jpg
convert input.jpg -edge 1 edges.jpg

# Create image montage
montage *.jpg -geometry 200x200+2+2 montage.jpg

# Extract image channels
convert input.jpg -separate channels_%d.jpg

# Composite images
composite overlay.png -gravity center base.jpg output.jpg
```

Watch this ImageMagick tutorial (16 min):

[[Image description: Here's alt text describing the image:

"A split screen image showcasing a geothermal area, possibly a geyser or hot spring.  The left side shows vibrant, almost surreal, yellows and greens in the water and surrounding land. The right side shows a more natural, muted palette of browns, tans, and whites, with steaming areas visible.  Both sides depict similar landscapes but with differing color saturation. A small wooden sign at the bottom right of the image reads 'Map of Africa.'  At the top of the image, in a large, stylized blue font on a slightly darker blue background, the words 'Image Magick Introduction' are displayed."]](https://youtu.be/wjcBOoReYc0)

Tools:

- [Fred's ImageMagick Scripts](http://www.fmwconcepts.com/imagemagick/): Useful script collection
- [ImageMagick Online Studio](https://magickstudio.imagemagick.org/): Visual command builder

Tips:

1. Use `-strip` to remove metadata and reduce file size
2. Monitor memory usage with `-limit memory 1GB`
3. Use `-define` for format-specific options
4. Process in parallel with `-parallel`
5. Use `-monitor` to track progress

Error Handling:

```bash
# Check image validity
identify -regard-warnings input.jpg

# Get detailed error information
convert input.jpg output.jpg 2&gt;&amp;1 | grep -i "error"

# Set resource limits
convert -limit memory 1GB -limit map 2GB input.jpg output.jpg
```

For Python integration:

```python
# /// script
# requires-python = "&gt;=3.9"
# dependencies = ["Wand"]
# ///

from wand.image import Image

async def process_image(path: str) -&gt; None:
    """Process image with ImageMagick via Wand."""
    with Image(filename=path) as img:
        # Basic operations
        img.resize(800, 600)
        img.normalize()

        # Apply effects
        img.sharpen(radius=0, sigma=3)

        # Save with compression
        img.save(filename='output.jpg')
```

Note: Always install ImageMagick before using the Wand Python binding.
