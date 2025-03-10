import svg
import os

from constants import *
from color_palette import COLOR_PALETTE as colors

hand1_element_list = [
    svg.Polygon(
        points = [
            centerX - hand1_width / 2    ,        centerY - hand_size,
            centerX                      ,        centerY - hand_size - hand1_tip,
            centerX + hand1_width / 2    ,        centerY - hand_size,
            centerX + hand1_width / 2    ,        centerY,
            centerX - hand1_width / 2    ,        centerY,
        ],
        fill = colors["instrument-hilt"],
    ),
    svg.Circle(
        cx = centerX, cy = centerY, r = hand_center_radius,
        fill = colors["instrument-bg"],
        stroke_width = stroke_w,
        stroke = colors["instrument-hilt"]
    ),
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
