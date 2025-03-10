import os
import svg
import numpy as np

from constants import *
from color_palette import COLOR_PALETTE as colors


def calculate_numbers():
    n_list = []
    for i in range(12):
        if (i % 3 == 0):
            continue
        else:
            n_list.append(i)

    print(n_list)
    return n_list


hsi_element_list = [
    svg.Circle(
        cx = centerX, cy = centerY, r = radius - stroke_w / 2,
        stroke = colors["instrument-hilt"], fill = colors["instrument-bg"],
        stroke_width = stroke_w,
    ),
]

small_tick_list = [
    svg.Rect(
        x = centerX - hsi_small_tick_width / 2,
        y = stroke_w + hsi_tick_spacing,

        width = hsi_small_tick_width, height = hsi_small_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i + (360 / (2*36)), centerX, centerY)
    )

    for i in np.linspace(0, 360, hsi_small_tick_number + 1)
]
hsi_element_list.extend(small_tick_list)

big_tick_list = [
    svg.Rect(
        x = centerX - hsi_big_tick_width / 2,
        y = stroke_w + hsi_tick_spacing,

        width = hsi_big_tick_width, height = hsi_big_tick_size,
        fill = colors["instrument-hilt"],
        transform = svg.Rotate(i, centerX, centerY)
    )

    for i in np.linspace(0, 360, hsi_big_tick_number + 1)
]
hsi_element_list.extend(big_tick_list)

letters_list = [
    svg.Text(
        x = centerX, y = hsi_font_spacing,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {hsi_font_size}px;",
        text = "N",
        transform = svg.Rotate(0, centerX, centerY),
    ),
    svg.Text(
        x = centerX, y = hsi_font_spacing,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {hsi_font_size}px;",
        text = "E",
        transform = svg.Rotate(90, centerX, centerY),
    ),
    svg.Text(
        x = centerX, y = hsi_font_spacing,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {hsi_font_size}px;",
        text = "S",
        transform = svg.Rotate(180, centerX, centerY),
    ),
    svg.Text(
        x = centerX, y = hsi_font_spacing,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {hsi_font_size}px;",
        text = "W",
        transform = svg.Rotate(270, centerX, centerY),
    ),
]
hsi_element_list.extend(letters_list)

numbers_list = [
    svg.Text(
        x = centerX, y = hsi_font_spacing,
        text_anchor = "middle",
        fill = colors["instrument-hilt"],
        style = f"font-family: {font_family}; font-size: {hsi_font_size}px;",
        text = str(i * 3),
        transform = svg.Rotate(i * (360 / 12), centerX, centerY),
    )

    for i in calculate_numbers()
]
hsi_element_list.extend(numbers_list)




hsi_canvas = svg.SVG(
    width = size,
    height = size,
    elements = hsi_element_list,
)


output_file = os.environ.get("OUTPUT_FILE", os.getcwd())

with open(output_file, "w") as file:
    file.write(hsi_canvas.as_str())

print(f"SVG file saved at: {output_file}")
