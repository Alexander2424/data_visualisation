# Data Visualisation
_July 2022_

Various scripts performing different types of data visualisation.

### Data visualised (by folder):
- #### alaska_vs_desert_weather:
  - Provides a coloured line chart with upper and lower temp. ranges comparing the temperatures between Alaska and Death Valley in 2018. The csv files included contain the source weather data for both geographies.
- #### github_popular_repos:
  - Produces interactive bar charts showing the most popular GitHub repositories for 7 different programming languages in real time by sourcing the bar chart data from GitHub via an API call. The _testing_popular_repos.py_ file contains a unit test to ensure that the API call is working and that the data returned conforms to the defined expectiations.
- #### hacker_news_submissions:
  - Produces an interactive bar chart showing the most discussed recent Hacker news submissions ranked by number of comments. Hovering over each bar will detail the name of the post, number of comments and provide a link to the actual post. The data is sourced from Hacker News website via an API call.
- #### visualising_random_walks:
  - _random_walk.py_ defines the class _RandomWalk()_ used to generate the random walks. The _pygal_randomwalk.py_ file uses the Python Pygal library and the class defined in _random_walk.py_ to generate the random walk plot _random_walk_visual.svg_. The _random_walk_plot.py_ file uses the Python Matplotlib library and the class defined in _random_walk.py_ to generate the random walk images _random_walk[0-3].png_.
- #### world_GDP:
  - The _world_gdp.py_ file uses the data stored in the json file _gdp.json_ and _world_ class from the Python Pygal library to generate the interactive .svg plot _world_gdp.svg_. The plot shows the world map with countries grouped and shaded by GDP, hovering the mouse over a country in the browser displays the country name and its gdp in dollars.
- #### world_population:
  - Similar to the _world_gdp.py_ file described above, the _world_population.py_ file generates the interactive _world_population.svg_ image that displays a world map with countries shaded and grouped by their population. The _country_codes.py_ file corrects some data issues in the source data imported from _pygal.maps.world_ _COUNTRIES_ so that all countries can be included in the world map image generated.
