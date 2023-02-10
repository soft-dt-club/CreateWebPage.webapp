from django.shortcuts import render,redirect
import re
import time
from django.views import View
from .form import searchForm
from .spotify import search

# Create your views here.

class MainView(View):
    
    def get(self,request):
      if "submit" in request.GET:
          return redirect('search')
      return render(request,'demo/index2.html')
    
    def form(request):
      form=searchForm()
      return render(request,'demo/index.html', {'form': form })


class LoadingView(View):
    
    def get(self,request):
      return render(request,'demo/results.html')

    @staticmethod
    def ajax_view(request):
        time.sleep(1)
        return render(request, 'demo/results.html')

class ResultView(View):

  def show(request):
    if request.method == 'POST':
      target=request.POST["keyword"]
      # 入力なしまたはスペースのみ指定した場合、結果画面を表示しない
      if not target or re.match('^[\s]+$', target):
        return redirect('search')
      else:
        return render(request, 'demo/results.html', {'keyword': target, 'list': search(target)})