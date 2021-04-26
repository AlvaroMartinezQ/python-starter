building_id = 12
building_name = "URJC-Library"
lat = 40.337088
lon = -3.875840

# f-string format
building_info = f'Building {building_id :04}. Name: {building_name}. GPS: {lat :.4f}, {lon :.4f}.'
print(building_info)

# multi line f-string format (readability)
building_info = (f'Building {building_id :04}.'
                    f' Name: {building_name}.'
                    f' GPS: {lat :.4f}, {lon :.4f}.'
)
print(building_info)
