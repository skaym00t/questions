from datetime import datetime, date, time

from django.db.models import Count, Q, F, Avg
from django.db.models.functions import ExtractWeek, ExtractWeekDay, ExtractQuarter, ExtractHour, ExtractMinute, \
    ExtractSecond

from questionapp.models import Author, Book, Review

# Базовые фильтры
john = Author.objects.filter(first_name='John')
any = Author.objects.exclude(last_name='Doe')

# Числовые сравнения

books_lt_500 = Book.objects.filter(price__lt = 500)
books_lte_300 = Book.objects.filter(price__lte=300)
books_gt_1000 = Book.objects.filter(price__gt = 1000)
books_gte_750 = Book.objects.filter(price__gte = 750)

# Поиск текста

books_django = Book.objects.filter(title__contains = 'django')
books_python = Book.objects.filter(title__icontains = 'python')
books_advanced = Book.objects.filter(title__startswith = 'Advanced')
books_pro = Book.objects.filter(title__istartswith = 'pro')
books_guide = Book.objects.filter(title__endswith = 'Guide')
books_tutorial = Book.objects.filter(title__iendswith = 'tutorial')

# Проверка на null

review_null = Review.objects.filter(comment__isnull = True)
review_not_null = Review.objects.filter(comment__isnull = False)

# IN и Range

author_id = Author.objects.filter(id__in = (1, 3, 5))
books_range_public = Book.objects.filter(published_date__range=(
    datetime(2023, 1, 1, 00, 00, 00),
    datetime(2023, 12, 31, 23, 59, 59)
    )
)

# Регулярные выражения

books_python_reg = Book.objects.filter(title__regex = r'^Python')
author_mc_reg = Author.objects.filter(last_name__iregex = r'^Mc')

# Даты и время

books_2024 = Book.objects.filter(published_date__year = 2024)
books_june = Book.objects.filter(published_date__month = 6)
review_11 = Review.objects.filter(created_at__day = 11)
books_week23 = Book.objects.annotate(week=ExtractWeek('published_date')).filter(week=23) # не знал про ExtractWeek
review_tuesday = Review.objects.annotate(weekday = ExtractWeekDay('created_at')).filter(weekday = 3) # не знал про ExtractWeekDay
reviews_2q = Review.objects.annotate(quarter=ExtractQuarter('created_at')).filter(quarter=2) # не знал ExtractQuarter
reviews_only_date = Review.objects.filter(created_at__date = date(2023, 6, 15))
reviews_only_time_15_30 = Review.objects.filter(created_at__time = time(15, 30))
reviews_only_time_15_00 = Review.objects.annotate(hours = ExtractHour('created_at')).filter(hours = 15) # не знал
reviews_only_30_min = Review.objects.annotate(minuts = ExtractMinute('created_at')).filter(minuts = 30) # не знал
reviews_only_00_sek = Review.objects.annotate(seconds = ExtractSecond('created_at')).filter(seconds = 00) # не знал

# Связанные поля

book_author = Book.objects.filter(author__email='author@example.com')
book_author_smith = Book.objects.filter(author__last_name__icontains='smith')
author_5_books = Author.objects.annotate(book_count=Count('books')).filter(book_count__gte=5)

# JSON-поля

fiction_books = Book.objects.filter(metadata__genre='fiction')
bestseller = Book.objects.filter(metadata__tags__icontains = 'bestseller')

# Использование выражений F и Q

books_discount_price = Book.objects.filter(price=F('discount'))
books_price_gt_discount = Book.objects.filter(price__gt=F('discount'))
authors = Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))

# Задания на аннотации

books_count = Author.objects.annotate(books_count=Count('books')).values('first_name', 'books_count')
books_avg_rating = Book.objects.annotate(avg_rating = Avg('reviews__rating')).values('title', 'avg_rating')
books_finish_price = Book.objects.annotate(fin_price = F('price') - F('discount')).values('title', 'fin_price')

# Использование select_related и prefetch_related

books_authors = Book.objects.all().select_related('author')
authors_books = Author.objects.all().prefetch_related('books')