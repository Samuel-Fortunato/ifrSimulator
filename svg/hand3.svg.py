import svg
import os

from constants import *
from color_palette import COLOR_PALETTE as colors

hand3_element_list = [
	svg.Polygon(
		points = [
			centerX + hand3_width / 2 			,		centerY,
			centerX - hand3_width / 2 			,		centerY,
			centerX - hand3_width / 2 			,		stroke_w + alt_big_spacing + hand3_tip,
			centerX - hand3_large_part / 2 		,		stroke_w + alt_big_spacing,
			centerX + hand3_large_part / 2 		,		stroke_w + alt_big_spacing,
			centerX + hand3_width / 2 			,		stroke_w + alt_big_spacing + hand3_tip,
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



hand3_canvas = svg.SVG(
    width = size,
    height = size,
    elements = hand3_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(hand3_canvas.as_str())

print(f"SVG file saved at: {output_file}")
