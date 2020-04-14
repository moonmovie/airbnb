from django.views.generic import ListView
from . import  models


class Homeview(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 3
    #page_kwarg ="changekword"
    
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
#from math import ceil

# Create your views here.

# pagination 1 
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]

#     page_count = ceil(models.Room.objects.count() / page_size)
#     return render(
#         request,
#         "rooms/home.html",
#         context={
#             "rooms": all_rooms,
#             "page": page,
#             "page_count": page_count,
#             "page_range": range(1, page_count + 1),
#         },
#     )

# pagination 2 paginator class 사용
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=3)
#     try:
#         rooms = paginator.page(page)
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")
    
#     print(vars(rooms.paginator))
#     print(vars(rooms))

