# Calculate state estimation using the power-grid-model library of a 3 bus network
# using Newton-Raphson method.

# Programmer: Oliver Gruber 29/6/2025

# Source of example power model: Power Grid Model project <powergridmodel@lfenergy.org>


import pandas as pd

from power_grid_model import (
    CalculationMethod,
    CalculationType,
    ComponentType,
    DatasetType,
    LoadGenType,
    MeasuredTerminalType,
    PowerGridModel,
    initialize_array,
)
from power_grid_model.validation import assert_valid_input_data

# node
node = initialize_array(DatasetType.input, ComponentType.node, 3)
node["id"] = [1, 2, 6]
node["u_rated"] = [10.5e3, 10.5e3, 10.5e3]

# line
line = initialize_array(DatasetType.input, ComponentType.line, 3)
line["id"] = [3, 5, 8]
line["from_node"] = [1, 2, 1]
line["to_node"] = [2, 6, 6]
line["from_status"] = [1, 1, 1]
line["to_status"] = [1, 1, 1]
line["r1"] = [0.25, 0.25, 0.25]
line["x1"] = [0.2, 0.2, 0.2]
line["c1"] = [10e-6, 10e-6, 10e-6]
line["tan1"] = [0.0, 0.0, 0.0]
line["i_n"] = [1000, 1000, 1000]

# load
sym_load = initialize_array(DatasetType.input, ComponentType.sym_load, 2)
sym_load["id"] = [4, 7]
sym_load["node"] = [2, 6]
sym_load["status"] = [1, 1]
sym_load["type"] = [LoadGenType.const_power, LoadGenType.const_power]
sym_load["p_specified"] = [20e6, 10e6]
sym_load["q_specified"] = [5e6, 2e6]

# source
source = initialize_array(DatasetType.input, ComponentType.source, 1)
source["id"] = [10]
source["node"] = [1]
source["status"] = [1]
source["u_ref"] = [1.0]

# voltage sensor
sym_voltage_sensor = initialize_array(DatasetType.input, ComponentType.sym_voltage_sensor, 3)
sym_voltage_sensor["id"] = [11, 12, 13]
sym_voltage_sensor["measured_object"] = [1, 2, 6]
sym_voltage_sensor["u_sigma"] = [1.0, 1.0, 1.0]
sym_voltage_sensor["u_measured"] = [10489.37, 9997.32, 10102.01]

# power sensor
sym_power_sensor = initialize_array(DatasetType.input, ComponentType.sym_power_sensor, 8)
sym_power_sensor["id"] = [14, 15, 16, 17, 18, 19, 20, 21]
sym_power_sensor["measured_object"] = [3, 3, 5, 5, 8, 8, 4, 6]
sym_power_sensor["measured_terminal_type"] = [
    MeasuredTerminalType.branch_from,
    MeasuredTerminalType.branch_to,
    MeasuredTerminalType.branch_from,
    MeasuredTerminalType.branch_to,
    MeasuredTerminalType.branch_from,
    MeasuredTerminalType.branch_to,
    MeasuredTerminalType.load,
    MeasuredTerminalType.node,
]
sym_power_sensor["power_sigma"] = [1.0e3, 1.0e3, 1.0e3, 1.0e3, 1.0e3, 1.0e3, 1.0e3, 1.0e3]
sym_power_sensor["p_measured"] = [1.73e07, -1.66e07, -3.36e06, 3.39e06, 1.38e07, -1.33e07, 20e6, -10e6]
sym_power_sensor["q_measured"] = [4.07e06, -3.82e06, -1.17e06, 8.86e05, 2.91e06, -2.88e06, 5e6, -2e6]

# all
input_data = {
    ComponentType.node: node,
    ComponentType.line: line,
    ComponentType.sym_load: sym_load,
    ComponentType.source: source,
    ComponentType.sym_voltage_sensor: sym_voltage_sensor,
    ComponentType.sym_power_sensor: sym_power_sensor,
}

# Validate data
assert_valid_input_data(input_data=input_data, calculation_type=CalculationType.state_estimation)

model = PowerGridModel(input_data, system_frequency=50.0)

output_data_NR = model.calculate_state_estimation(symmetric=True, calculation_method=CalculationMethod.newton_raphson)

print("""
Node result""")
print(pd.DataFrame(output_data_NR[ComponentType.node]))

print("""
Line result""")
print(pd.DataFrame(output_data_NR[ComponentType.line]))

print("""
Sym_load result""")
print(pd.DataFrame(output_data_NR[ComponentType.sym_load]))


