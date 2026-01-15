size = 512

centerX = size / 2
centerY = size / 2

radius = size / 2

stroke_w = size / 64

alt_big_tick_size = size / 16
alt_big_spacing = size / 64
alt_big_tick_number = 10
alt_big_tick_width = stroke_w

alt_small_tick_size = size / 32
alt_small_spacing = size / 32
alt_small_tick_number = 50
alt_small_tick_width = stroke_w / 2

window_size_x = (1/8) * size
window_size_y = (3/4) * window_size_x
window_position_x = (3/4) * size
window_padding = size / 64

pointer_size_x = size / 16
pointer_size_y = stroke_w
arrow_size = pointer_size_x / 2



alt_font_size = int(size / 8)
alt_txt_radius = (5/8) * radius
prss_font_size = int(window_size_x / 4)
prss_txt_x = window_size_x / 16

font_family = f"Arial, sans-serif"


prss_min = 925
prss_big_scale = 5

prss_big_tick_size = window_size_x / 4
prss_big_spacing_right = window_size_x / 16
prss_big_tick_width = stroke_w / 4
prss_big_tick_number = 30

prss_small_tick_size = window_size_x / 8
prss_small_spacing_right = window_size_x / 16
prss_small_tick_width = stroke_w / 8
prss_small_tick_number = 150


hand_width = size / 16
hand_size = radius / 2
hand_center_radius = hand_width / 2
hand_center_stroke = stroke_w 

hand1_width = hand_width / 2
hand1_tip = hand_size / 8

hand2_width = hand_width / 2
hand2_tip = hand_size * (3/4)
hand2_large_part = hand2_width * 3

hand3_width = hand_width / 4
hand3_tip = radius / 8
hand3_large_part = hand3_tip



hsi_font_size = int(size / 10)
hsi_font_spacing = size / 5

hsi_tick_spacing = size / 64

hsi_small_tick_width = stroke_w / 2
hsi_small_tick_size = size / 32
hsi_small_tick_number = 36

hsi_big_tick_width = stroke_w
hsi_big_tick_size = size / 16
hsi_big_tick_number = 36

hsi_marker_width = stroke_w
hsi_marker_size = size / 16


spd_begin = 40
spd_end = 200
spd_begin_angle = 45
spd_end_angle = 315
max_speed = 158
max_speed_angle = spd_begin_angle + ((spd_end_angle - spd_begin_angle) / (spd_end - spd_begin)) * (max_speed - spd_begin)

spd_big_tick_size = size / 10
spd_big_spacing = 0
spd_big_tick_number = 17
spd_big_tick_width = stroke_w

spd_small_tick_size = size / 20
spd_small_spacing = 0
spd_small_tick_number = 33
spd_small_tick_width = stroke_w / 2