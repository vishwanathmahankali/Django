from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import ReviewForm
# Create your views here.

class ReviewView(CreateView):
    
    form_class = ReviewForm
    model = Review
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    # def get(self, request):
    #     form = ReviewForm()
    
    #     return render(request, "reviews/review.html", {
    #         "form": form,
    #     })
    
    # def post(self, request):
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {
    #         "form": form,
    #     })
    
    
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
        
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review 


    


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favors_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)