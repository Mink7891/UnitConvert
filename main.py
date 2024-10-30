import dearpygui.dearpygui as dpg

dpg.create_context()

window_width = 500
window_height = 250

dpg.create_viewport(title="UnitConvert", decorated=True)
dpg.configure_viewport(0, x_pos=100, y_pos=100, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

def convert_units():
    unit_type = dpg.get_value("unit_selector")
    value = dpg.get_value("input_value")
    
    dpg.set_value("result_text", "")
    
    if unit_type == "Kilograms":
        grams = value * 1000
        tonnes = value / 1000
        pounds = value * 2.20462
        dpg.set_value("result_text", f"{value} kg = {grams} g\n{value} kg = {tonnes} tonnes\n{value} kg = {pounds:.2f} lbs")
    
    elif unit_type == "Meters":
        centimeters = value * 100
        kilometers = value / 1000
        feet = value * 3.28084
        inches = value * 39.3701
        dpg.set_value("result_text", f"{value} m = {centimeters} cm\n{value} m = {kilometers} km\n{value} m = {feet:.2f} feet\n{value} m = {inches:.2f} inches")
    
    elif unit_type == "Liters":
        milliliters = value * 1000
        cubic_meters = value / 1000
        gallons = value * 0.264172
        dpg.set_value("result_text", f"{value} L = {milliliters} mL\n{value} L = {cubic_meters} m³\n{value} L = {gallons:.2f} gallons")

    elif unit_type == "Celsius":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        dpg.set_value("result_text", f"{value} °C = {fahrenheit:.2f} °F\n{value} °C = {kelvin:.2f} K")

with dpg.window(width=window_width, height=window_height) as main_window:

    dpg.add_combo(["Kilograms", "Meters", "Liters", "Celsius"], 
                  label="Unit Type", tag="unit_selector", width=200, indent=20)

    dpg.add_input_float(label="Enter Value", tag="input_value", width=200, indent=20)
    
    dpg.add_button(label="Convert", width=150, height=30, indent=20, callback=convert_units)
    
    dpg.add_text("", tag="result_text", color=(0, 200, 0), indent=20)

dpg.set_primary_window(main_window, True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
