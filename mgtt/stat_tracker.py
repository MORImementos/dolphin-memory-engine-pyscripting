from addresses import mgtt_addresses as mgtt

def print_on_change(variable_name, current_value, previous_values):
    if variable_name not in previous_values or previous_values[variable_name] != current_value:
        print(f"{variable_name}: {current_value}")
        previous_values[variable_name] = current_value


previous_values = {}

while True:
    # if mgtt.player_shot_number[0].read() == 213:
    #     print('not in game')
    # else:
    if mgtt.player_count.read() > 0 and mgtt.round_format.read() > 0 and mgtt.current_hole.read() == 0 and mgtt.player_shot_number[0].read() == 0:
        row = []
        labels = ['player_count:', 'round_format:', 'course_id:', 'green_type:', 'tee:', 'char/star/hand:']
        row.append(mgtt.player_count.read())
        row.append(mgtt.round_format.read())
        row.append(mgtt.course_id.read())
        row.append(mgtt.green_type.read())
        row.append(mgtt.tee.read())
        row.append((mgtt.char_selection_menu[0].read(), mgtt.char_star_menu[0].read(), mgtt.char_hand_menu[0].read()))
        # print_on_change("current_shot_number", mgtt.player_shot_number[0].read(), previous_values)
        # print_on_change("player_turn", mgtt.player_turn.read(), previous_values)
        # print_on_change('accuracy', mgtt.shot_accuracy.read(), previous_values)
        # print_on_change('player count', mgtt.player_count.read(), previous_values)
        # print_on_change('round format', mgtt.round_format.read(), previous_values)
        for i in range(0, len(row)):
            print(labels[i], row[i])
        break
    print_on_change()
