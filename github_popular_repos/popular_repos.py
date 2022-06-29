import requests
import pygal
from visual_settings import my_config, my_style

# Make and API call and store the respone.
languages = ["Python", "JavaScript", "Ruby", "C", "Java", "Haskell", "Go"]

for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    r = requests.get(url)
    print("Status code:", r.status_code)

    # Store API response in a variable.
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    # Process results.
    # print(response_dict.keys())

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    # print("Repositories returned:", len(repo_dicts))

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = f"Most-Starred {language} Projects on Github"
    chart.x_labels = names

    chart.add('', plot_dicts)
    filename = f"{language}_repos.svg"
    chart.render_to_file(filename)