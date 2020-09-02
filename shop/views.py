from django.shortcuts import render, get_object_or_404
from .models import *

def shop_home(request):
    # get category lists
    categories = ProductCategory.objects.all()

    products = Product.objects.all()
    reviews_list = []
    for product in products:
        review_star = 0
        count = 0
        reviews = product.productreview_set.all()
        for review in reviews:
            review_star += review.review_score
        if reviews.count() != 0:
            review_star = review_star / reviews.count()
        reviews_list.append(review_star)
    product_review_dict = dict(zip(products, reviews_list))
    
    context = {
        'products': products,
        'product_review_dict': product_review_dict,
        'categories': categories
    }
    return render(request, template_name='shop/shop_home.html', context=context)

def shop_item_details(request, pk):
    # get category lists
    categories = ProductCategory.objects.all()

    product = get_object_or_404(Product, id=pk)

    review_score= 0
    count = 0
    reviews_data = []
    reviews = product.productreview_set.all()
    reviews_count = reviews.count()
    for review in reviews:
        # add reviews data to reviews_data
        reviews_data_list = []
        reviews_data_list.append(review.author_name)
        reviews_data_list.append(review.review_score)
        reviews_data_list.append(review.review_description)
        reviews_data.append(reviews_data_list)

        review_score += review.review_score
        
    if reviews_count != 0:
        review_score = review_score/ reviews_count

    context = {
        'product': product,
        'title': product.product_name,
        'review_score': review_score,
        'total_reviews': reviews_count,
        'reviews': reviews_data,
        'categories': categories
    }
    return render(request, template_name='shop/shop_item_details.html', context=context)


def shop_category(request, pk):
    
    # get category lists
    categories = ProductCategory.objects.all()

    category = ProductCategory.objects.get(id=pk)

    products = Product.objects.filter(categories=category).all()

    reviews_list = []
    for product in products:
        review_star = 0
        count = 0
        reviews = product.productreview_set.all()
        for review in reviews:
            review_star += review.review_score
        if reviews.count() != 0:
            review_star = review_star / reviews.count()
        reviews_list.append(review_star)
    product_review_dict = dict(zip(products, reviews_list))
    
    context = {
        'products': products,
        'product_review_dict': product_review_dict,
        'categories': categories,
        'current_category': category
    }

    return render(request, template_name="shop/shop_category.html", context=context)