import os
import svg

from constants import *
from color_palette import COLOR_PALETTE as colors

hsi_element_list = [
	svg.Defs(
        elements = [
            svg.Mask(
                id = "circle",
                elements = [
                    svg.Rect(
                        x = 0, y = 0, width = size, height = size,
                        fill = "white",
                    ),
                    svg.Circle(
                        cx = centerX, cy = centerY,
                        r = radius,
                        fill = "black",
                    )
                ]
            )
        ]
    ),

    svg.Rect(
        x = 0, y = 0, width = size, height = size,
        fill = colors["panel"],
        mask = "url(#circle)"
    ),

    svg.Polygon(
        points = [
            centerX + size / 8      ,       -30+ centerY + size / 32,
            centerX + size / 8      ,       -30+ centerY - size / 32,
            centerX + size / 32     ,       -30+ centerY - size / 32,
            centerX                 ,       -30+ centerY - size / 8,
            centerX - size / 32     ,       -30+ centerY - size / 32,
            centerX - size / 8      ,       -30+ centerY - size / 32,
            centerX - size / 8      ,       -30+ centerY + size / 32,
            centerX - size / 32     ,       -30+ centerY + size / 32,
            centerX - size / 32     ,       -30+ centerY + size / 8,
            centerX - size / 16     ,       -30+ centerY + size / 8,
            centerX - size / 16     ,       -30+ centerY + size / 6,
            centerX + size / 16     ,       -30+ centerY + size / 6,
            centerX + size / 16     ,       -30+ centerY + size / 8,
            centerX + size / 32     ,       -30+ centerY + size / 8,
            centerX + size / 32     ,       -30+ centerY + size / 32,
        ],
        fill = colors["instrument-hilt-2"],
    )
]

markers_list = [
	svg.Rect(
		x = centerX - hsi_marker_width / 2, y = stroke_w,
		width = hsi_marker_width, height = hsi_marker_size,
		fill = colors["instrument-hilt-2"],
		transform = svg.Rotate(i, centerX, centerY),
	)

	for i in range(0, 359, 45)
]
hsi_element_list.extend(markers_list)



hsi_canvas = svg.SVG(
    width = size,
    height = size,
    elements = hsi_element_list,
)


output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(hsi_canvas.as_str())

print(f"SVG file saved at: {output_file}")
