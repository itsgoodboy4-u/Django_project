from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    peoples = [
        {"name":'A', 'age': 23},
        {"name":'B', 'age': 16},
        {"name":'C', 'age': 25},
        {"name":'D', 'age': 14},
        {"name":'E', 'age': 23}
    ]
    text = '''
            Cupa  it deserunt sunt esse occaecat excepteur. Anim ea incididunt non aliquip.

            Non et excepteur in veniam commodo in id. Deserunt ex dolore incididunt voluptate id irure. Ipsum cupidatat eu excepteur reprehenderit ipsum qui eu quis adipisicing elit dolore voluptate sit sit. Deserunt tempor in duis eu dolor nostrud ea est nostrud mollit ullamco. Ipsum et eiusmod et elit voluptate dolor ullamco mollit cillum dolore.

            Esse occaecat mollit labore aliquip do ullamco elit dolore dolor reprehenderit sit reprehenderit in laborum. Cillum non excepteur eu reprehenderit elit minim ut. Quis aliquip anim ullamco consectetur in est qui.
        '''
    # return HttpResponse("Hello, this is the polls index. ")
    return render(request, "home/index.html", context = {'peoples' : peoples, 'text': text})




