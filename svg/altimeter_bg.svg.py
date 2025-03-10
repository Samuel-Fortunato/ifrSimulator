import os
import numpy as np
import math
import svg

from constants import *
from color_palette import COLOR_PALETTE as colors

def calculate_text_x(i):
    return centerX + alt_txt_radius * math.sin(i * ((2 * math.pi) / alt_big_tick_number))

def calculate_text_y(i):
    return centerY - alt_txt_radius * math.cos(i * ((2 * math.pi) / alt_big_tick_number))


bg_element_list = [
    svg.Defs(
        elements = [
            # pressure rectangle mask
            svg.Mask(
                id = "pressureRect",
                elements = [
                    svg.Rect(
                        x = 0, y = 0, width = size, height = size,
                        fill = "white",
                    ),
                    svg.Rect(
                        x = window_position_x, y = centerY - window_size_y / 2 + window_padding,
                        width = window_size_x, height = window_size_y,
                        fill = "black",
                    )
                ]
            )
        ]
    ),

    # background
    svg.Rect(
        x = 0, y = 0, width = size, height = size,
        fill = colors["panel"],
        mask = "url(#pressureRect)"
    ),

    # altimeter circle
    svg.Circle(
        cx = centerX, cy = centerY, r = radius - stroke_w / 2,
        stroke = colors["instrument-hilt"], fill = colors["instrument-bg"],
        stroke_width = stroke_w,
        mask = "url(#pressureRect)"
    ),

    # pressure rectangle
    svg.Rect(
        x = window_position_x, y = centerY - window_size_y / 2 + window_padding,
        width = window_size_x, height = window_size_y,
        stroke = colors["instrument-hilt"],
        stroke_width = stroke_w / 2,
        mask = "url(#pressureRect)"
    ),

    # pressure pointer
    svg.Rect(
        x = size - pointer_size_x - stroke_w - alt_big_spacing, y = centerY - pointer_size_y / 2 + window_padding,
        width = pointer_size_x, height = pointer_size_y,
        fill = colors["instrument-hilt"]
    ),
    svg.Polygon(
        points = [
            size - pointer_size_x - stroke_w - alt_big_spacing,                     centerY - pointer_size_y / 2 + window_padding,
            size - pointer_size_x - stroke_w - alt_big_spacing,                     centerY - pointer_size_y / 2 + window_padding + pointer_size_y,
            size - pointer_size_x - stroke_w - alt_big_spacing - arrow_size,       centerY - pointer_size_y / 2 + window_padding + pointer_size_y / 2,
        ],
        fill = colors["instrument-hilt"]
    )
]

# small ticks
alt_small_ticks_list = [
    svg.Rect(
        x = centerX - alt_small_tick_width / 2,
        y = stroke_w + alt_small_spacing,

        width = alt_small_tick_width, height = alt_small_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i, centerX, centerY)
    )

    for i in np.linspace(0, 360, alt_small_tick_number + 1)
]
bg_element_list.extend(alt_small_ticks_list)

# big ticks
alt_big_ticks_list = [
    svg.Rect(
        x = centerX - alt_big_tick_width / 2,
        y = stroke_w + alt_big_spacing,

        width = alt_big_tick_width, height = alt_big_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i, centerX, centerY)
    )

    for i in np.linspace(0, 360, alt_big_tick_number + 1)
]
bg_element_list.extend(alt_big_ticks_list)

# numbers
bg_text_list = [
    svg.Text(
        x = calculate_text_x(i), y = calculate_text_y(i) + alt_font_size / 2,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {alt_font_size}px;",
        text = str(i)
    )

    for i in range(alt_big_tick_number)
]
bg_element_list.extend(bg_text_list)




bg_canvas = svg.SVG(
    width = size,
    height = size,
    elements = bg_element_list,
)

output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(bg_canvas.as_str())

print(f"SVG file saved at: {output_file}")
