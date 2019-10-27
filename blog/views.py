from django.shortcuts import render
import requests
# from django.http import HttpResponse
# Create your views here.
all_post = requests.get('https://trinity-twitter-apiv3.appspot.com/').json()[:10]
# list_post
posts = []
count_feel = 0
for i in range(len(all_post)):
    if all_post[i]['api']['word_feel'] == 'good':
        count_feel += 1
count_feel_good = str(int((count_feel/len(all_post))*100)) + '%'
count_feel_bad = str(int(100-((count_feel/len(all_post))*100))) + '%'

for i in range(len(all_post)):
    posts.append(
        {
            'author': all_post[i]['api']['author_link_post'],
            'title': all_post[i]['api']['author_name'],
            'content': all_post[i]['api']['author_description'],
            'date_posted': all_post[i]['api']['time_day'] + '/' + all_post[i]['api']['time_month'] + '/' +all_post[i]['api']['time_year'],
            'feel':all_post[i]['api']['word_feel'],
        }
    )



    # posts = [
    #     {
    #         'author': all_post[0]['api']['list_hash_tag'],
    #         'title': all_post[0]['api']['header'],
    #         'content': all_post[0]['api']['description_comment'],
    #         'date_posted': all_post[0]['api']['day'] + '/' + all_post[0]['api']['month'] + '/' +all_post[0]['api']['year']
    #     }
    # ]
# posts = [
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
def home(request):
    context = {
        'posts': posts,
        'count_feel_good':count_feel_good,
        'count_feel_bad':count_feel_bad
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})