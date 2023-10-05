import pypyodbc
drivers_list = sorted(pypyodbc.drivers())
for driver_name in drivers_list:
    print(driver_name)