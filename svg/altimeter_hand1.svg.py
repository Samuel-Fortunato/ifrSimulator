import svg
import os

from altimeter_constants import *
from color_palette import COLOR_PALETTE as colors

hand1_element_list = [
    svg.Polygon(
        points = [
            centerX - hand1_width / 2   ,        stroke_w + big_tick_size + 2 * big_spacing + hand1_tip,
            centerX                     ,        stroke_w + big_tick_size + 2 * big_spacing,
            centerX + hand1_width / 2   ,        stroke_w + big_tick_size + 2 * big_spacing + hand1_tip,
            centerX + hand1_width / 2   ,        centerY,
            centerX - hand1_width / 2   ,        centerY,
        ],
        fill = "white"
    )
]





hand1_canvas = svg.SVG(
    width = size,
    height = size,
    elements = hand1_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(hand1_canvas.as_str())

print(f"SVG file saved at: {output_file}")
