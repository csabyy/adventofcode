from common import *


def apply_button_to_current_light_state(current_state, button_to_apply):
    new_current_state = set(current_state)
    for btn in button_to_apply:
        if btn in new_current_state:
            new_current_state.remove(btn)
        else:
            new_current_state.add(btn)
    return new_current_state


def are_lights_equal(current_state, target_state):
    if len(current_state) != len(target_state):
        return False
    for target in target_state:
        if target not in current_state:
            return False
    return True


def process_light(initial_state, target_state):
    presses = [initial_state]
    while len(presses) > 0:
        current_state = presses.pop(0)
        for button_ix, button in enumerate(current_state[1]):
            new_current_state = apply_button_to_current_light_state(current_state[0], button)
            if are_lights_equal(new_current_state, target_state):
                return current_state[2]
            presses.append((new_current_state, current_state[1][button_ix + 1:], current_state[2] + 1))


def process_lights(config_values):
    result = 0
    for config_value in config_values:
        result += process_light(({}, config_value.button_config, 1), config_value.light_config)
    return result


def main():
    print(process_lights(load_config_from_file("input.txt")))


if __name__ == "__main__":
    main()
