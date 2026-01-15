import svg
import os

from constants import *
from color_palette import COLOR_PALETTE as colors

hand2_element_list = [
	svg.Polygon(
		points = [
			centerX - hand2_width / 2 			,		centerY,
			centerX + hand2_width / 2 			,		centerY,
			centerX + hand2_large_part / 2 		,		centerY - hand2_tip,
			centerX								,		centerY - hand_size,
			centerX - hand2_large_part / 2 		,		centerY - hand2_tip,
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


hand2_canvas = svg.SVG(
    width = size,
    height = size,
    elements = hand2_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(hand2_canvas.as_str())

print(f"SVG file saved at: {output_file}")
