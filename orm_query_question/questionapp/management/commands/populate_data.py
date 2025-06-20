from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
import decimal
from datetime import datetime, timedelta
from ...models import Book, Author, Review
import time


class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Очистка данных
        Review.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Создаем авторов
        authors = []
        for _ in range(10):
            author = Author.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                is_active=random.choice([True, False])
            )
            authors.append(author)
            self.stdout.write(f'Created author: {author.first_name} {author.last_name}')

        # Создаем книги
        books = []
        for _ in range(30):
            author = random.choice(authors)
            published_date = fake.date_time_between(
                start_date='-10y',
                end_date='now'
            )

            book = Book.objects.create(
                title=fake.sentence(nb_words=4),
                author=author,
                published_date=timezone.make_aware(published_date),
                price=decimal.Decimal(random.randrange(100, 5000) / 100),
                discount=decimal.Decimal(random.randrange(0, 2000) / 100),
                metadata={
                    'genre': random.choice(['Фантастика', 'Детектив', 'Роман', 'Научная', 'Исторический']),
                    'pages': random.randint(100, 800),
                    'publisher': fake.company()
                }
            )
            books.append(book)
            self.stdout.write(f'Created book: {book.title} by {author.last_name}')

        # Создаем отзывы с уникальными датами
        for book_index, book in enumerate(books):
            review_count = random.randint(1, 5)

            # Базовое время для отзывов этой книги - случайное в пределах года
            base_date = timezone.make_aware(fake.date_time_between(
                start_date=book.published_date,
                end_date='now'
            ))

            for review_index in range(review_count):
                # Случайное смещение: от 1 минуты до 30 дней
                time_offset = timedelta(
                    days=random.randint(0, 30),
                    hours=random.randint(0, 24),
                    minutes=random.randint(0, 60),
                    seconds=random.randint(0, 60),
                    milliseconds=random.randint(0, 1000),
                )

                # Для каждого следующего отзыва смещаемся назад во времени
                created_at = base_date - time_offset * (review_index + 1)

                # Добавляем дополнительное случайное смещение
                random_offset = timedelta(
                    seconds=random.randint(0, 3600),  # до 1 часа
                    milliseconds=random.randint(0, 1000),
                )
                created_at -= random_offset

                # Гарантируем, что дата не раньше публикации книги
                if created_at < book.published_date:
                    created_at = book.published_date + timedelta(days=1)

                Review.objects.create(
                    book=book,
                    rating=random.randint(1, 5),
                    comment=fake.paragraph(nb_sentences=3) if random.random() > 0.3 else None,
                    created_at=created_at
                )

            self.stdout.write(f'Added {review_count} reviews for: {book.title}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))