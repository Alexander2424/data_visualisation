import json

import pygal.maps.world as pyworld

from country_codes import get_country_code as gcc
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

# Load the data into a list.
filename = 'gdp.json'
with open(filename) as f:
	gdp_data = json.load(f)

# Build a dictionary of population data.
cc_gdp = {}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2016:
		country_name = gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		code = gcc(country_name)
		if code:
			cc_gdp[code] = gdp

# Group the countries into 3 population levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
	if gdp < 1000000000000:
		cc_gdp_1[cc] = gdp
	elif gdp < 10000000000000:
		cc_gdp_2[cc] = gdp
	else:
		cc_gdp_3[cc] = gdp

# See how many countries are in each level.
#print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pyworld.World(style=wm_style)
# wm = pyworld.World()
wm.title = 'World GDP in 2016, by Country'
# wm.add('gdp values',cc_gdp)
wm.add('0-$1trn', cc_gdp_1)
wm.add('$1trn-$10trn', cc_gdp_2)
wm.add('>$10trn', cc_gdp_3)

wm.render_to_file('world_gdp.svg')
