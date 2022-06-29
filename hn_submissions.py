from operator import itemgetter

import requests
import pygal
from visual_settings import my_config, my_style

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

names, plot_dicts = [], []
for submission_dict in submission_dicts:
    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")
    names.append(submission_dict['title'])

    plot_dict = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['hn_link'],
    }
    plot_dicts.append(plot_dict)

chart = pygal.Bar(my_config, style=my_style)

chart.title = "Most active Hacker News discussions"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file("hn_submissions.svg")
