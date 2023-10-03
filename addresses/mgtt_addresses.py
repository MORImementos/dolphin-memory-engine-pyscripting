from memory_engine import *


# menu tracking
char_selection_menu = [
    DolphinByte(0x8044BA48)
]

char_star_menu = [
    DolphinByte(0x8044ba68)
]

char_hand_menu = [
    DolphinByte(0x804f205e)
]

# round tracking
course_id = DolphinByte(0x8044afdf)
round_format = DolphinByte(0x8044afe7)
green_type = DolphinByte(0x8044bd9b)
tee = DolphinByte(0x8044afe3)
player_count = DolphinByte(0x804E68FA)

# hole tracking
player_turn = DolphinByte(0x804E68FB)
current_hole = DolphinByte(0x804e674b)
player_turn_number = DolphinByte(0x804e68f8)
wind_heading_rad = DolphinFloat(0x804e6850)
wind_speed_mps = DolphinFloat(0x804e6854)
rain_bool = DolphinBool(0x804e6858)
pin = DolphinByte(0x804e6714)
pin_second_value = DolphinWord(0x804e66ac)

pin_coordinates = [
    DolphinFloat(0x804e6864),
    DolphinFloat(0x804e6868),
    DolphinFloat(0x804e686c)
]

# player tracking
player_shot_number = [
    DolphinByte(0x806cb4fc),
    DolphinByte(0x806cb6c4),
    DolphinByte(0x806cb88c),
    DolphinByte(0x806cba54)
]

player_port_number = [
    DolphinByte(0x804E6674),
    DolphinByte(0x804E6675),
    DolphinByte(0x804E6676),
    DolphinByte(0x804E6677)
]

player_ball_coordinates = [
    [
        DolphinFloat(0x805dc0b0),
        DolphinFloat(0x805dc0c0),
        DolphinFloat(0x805dc0d0)
    ],
    [],
    [],
    []
]

sim_line_end_coordinates = [
    DolphinFloat(0x804ECD70),
    DolphinFloat(0x804ECD74),
    DolphinFloat(0x804ECD78)
]

# shot tracking
shot_type = DolphinWord(0x804ecd50)
club_type = DolphinWord(0x804ecd58)
power_meter_player_set = DolphinWord(0x804e3658)
power_meter_player_set_copy = DolphinWord(0x804ecd54)
power_meter_max_length = DolphinWord(0x804ecdd4)
power_meter_power = DolphinWord(0x804e6768)
power_meter_power_copy = DolphinWord(0x804ecd1c)
shot_accuracy = DolphinWord(0x80523cac)
# check data type
shot_accuracy_2 = DolphinWord(0x804ECD30)

manual_auto = DolphinWord(0x804ecd88)
aim_angle_radians = DolphinFloat(0x804ecd5c)
impact_point_y_preshot = DolphinWord(0x804ECDA0)
impact_point_x_preshot = DolphinWord(0x804ECDA4)
impact_point_x = DolphinWord(0x804ecdac)
impact_point_y = DolphinWord(0x804ecda8)
spin = DolphinWord(0x804ecd4c)
# check data type
distance_to_hole = DolphinFloat(0x802D7368)

# lie tracking
lie_id = DolphinWord(0x804e364c)
lie_quality = DolphinWord(0x804e3650)
lie_rng_range = DolphinWord(0x804ecdbc)
lie_rng = DolphinWord(0x804ecdc0)
lie_rng_seed = DolphinWord(0x804ecd3c)

# state tracking
shot_stage = DolphinWord(0x804ecdd0)
is_golf_match = DolphinWord(0x80162B5F)

