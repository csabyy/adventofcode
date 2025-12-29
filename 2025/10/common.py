import re


class ConfigValue:
    def __init__(self, light_config, button_config, joltage_config):
        self.light_config = light_config
        self.button_config = button_config
        self.joltage_config = joltage_config

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"ConfigValue({self.light_config}, {self.button_config}, {self.joltage_config})"


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def load_config_from_file(filename):
    with open(filename, "r") as file:
        config_values = []
        for line in file:
            light_config = set(find(line[(re.search("\\[.*]", line).span()[0] + 1):], "#"))
            button_config = []
            for button in re.findall("(?<=\\()(.*?)(?=\\))", line):
                button_lights = []
                for btn in button.split(","):
                    button_lights.append(int(btn))
                button_config.append(button_lights)
            joltage_config = {}
            for joltage_ix, joltage in enumerate(re.search("\\{.*}", line).group()[1:-1].split(",")):
                joltage_config[joltage_ix] = int(joltage)
            config_value = ConfigValue(light_config, button_config, joltage_config)
            config_values.append(config_value)

        return config_values
