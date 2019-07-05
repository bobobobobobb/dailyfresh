from django.shortcuts import render, redirect
from django.views import View
from books.models import BookInfo, HeroInfo
from django.http import JsonResponse


class IndexView(View):
    def get(self, request):
        books = BookInfo.objects.all()

        return render(request, 'index.html', {'books': books})


class HeroinfoView(View):
    def get(self, request, book_id):
        heros = HeroInfo.objects.filter(hbook_id=book_id)
        hero_dict = []
        dict_info = {}
        for hero in heros:
            # dict_info[hero.id] = hero.hname
            # hero_dict.append(dict_info)
            # dict_info = {}
            hero_dict.append({"id": hero.id,"hname":hero.hname})
        print(hero_dict)
        return JsonResponse({'heros': hero_dict})
