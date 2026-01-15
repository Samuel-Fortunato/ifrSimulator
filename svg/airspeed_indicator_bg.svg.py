import os
import svg
import numpy as np
import math

from constants import *
from color_palette import COLOR_PALETTE as colors

airspeed_element_list = [
	svg.Rect(
		x = 0, y = 0,
		width = size, height = size,
		fill = colors["panel"],
	),

	svg.Circle(
		cx = centerX, cy = centerY, r = radius,
		stroke_width = stroke_w, stroke = colors["instrument-hilt"],
	),

	svg.Rect(
		x = centerX - spd_small_tick_width / 2,
        y = stroke_w + spd_big_spacing,

        width = spd_small_tick_width, height = spd_big_tick_size,

        fill = "red",
        transform = svg.Rotate(max_speed_angle, centerX, centerY),
	),
]


small_ticks_list = [
    svg.Rect(
        x = centerX - spd_small_tick_width / 2,
        y = stroke_w + spd_small_spacing,

        width = spd_small_tick_width, height = spd_small_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i, centerX, centerY)
    )

    for i in np.linspace(spd_begin_angle, spd_end_angle, spd_small_tick_number)
]
airspeed_element_list.extend(small_ticks_list)

big_ticks_list = [
    svg.Rect(
        x = centerX - spd_big_tick_width / 2,
        y = stroke_w + spd_big_spacing,

        width = spd_big_tick_width, height = spd_big_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i, centerX, centerY)
    )

    for i in np.linspace(spd_begin_angle, spd_end_angle, spd_big_tick_number)
]
airspeed_element_list.extend(big_ticks_list)





airspeed_canvas = svg.SVG(
    width = size,
    height = size,
    elements = airspeed_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(airspeed_canvas.as_str())

print(f"SVG file saved at: {output_file}")
