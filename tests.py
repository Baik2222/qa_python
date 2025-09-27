import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Простая книга', 'Книга ' + ('A' * 34)])
    def test_add_new_book_name_length_40_or_less(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name in collector.get_books_genre()

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()

        long_name = 'A' * 50
        collector.add_new_book(long_name)

        assert long_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()

        title = 'Преступление и наказание'
        collector.add_new_book(title)
        collector.add_new_book(title)

        assert list(collector.get_books_genre().keys()).count(title) == 1

    @pytest.mark.parametrize('genre', ['Детективы', 'Мультфильмы'])
    def test_set_book_genre_success(self, genre):
        collector = BooksCollector()

        title = 'Мёртвые души'
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)

        assert collector.get_book_genre(title) == genre

    def test_set_book_genre_not_in_genre_list(self):
        collector = BooksCollector()

        title = 'Дубровский'
        collector.add_new_book(title)
        collector.set_book_genre(title, 'Романтика')
        assert collector.get_book_genre(title) == ''

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()

        title = 'Код Отчаяния'
        collector.set_book_genre(title, 'Фантастика')
        assert collector.get_book_genre(title) is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        title_1 = 'Мёртвые души'
        title_2 = 'Дубровский'
        genre = 'Детективы'

        collector.add_new_book(title_1)
        collector.add_new_book(title_2)
        collector.set_book_genre(title_1, genre)
        collector.set_book_genre(title_2, genre)
        books = collector.get_books_with_specific_genre(genre)

        assert set(books) == {title_1, title_2}

    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        books = collector.get_books_with_specific_genre('Комедии')

        assert books == []

    def test_get_books_genre(self):
        collector = BooksCollector()

        title = 'Преступление и наказание'
        collector.add_new_book(title)

        assert isinstance(collector.get_books_genre(), dict)
        assert title in collector.get_books_genre()

    def test_get_books_for_children_filters_age_rating(self):
        collector = BooksCollector()

        title_1 = 'Маленький принц'
        title_2 = 'Оно'

        collector.add_new_book(title_1)
        collector.add_new_book(title_2)
        collector.set_book_genre(title_1, 'Мультфильмы')
        collector.set_book_genre(title_2, 'Ужасы')
        books = collector.get_books_for_children()

        assert title_1 in books
        assert title_2 not in books

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()

        title = 'Маленький принц'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)

        assert title in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()

        title = 'Оно'
        collector.add_book_in_favorites(title)

        assert title not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()

        title = 'Маленький принц'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)
        collector.add_book_in_favorites(title)
        assert collector.get_list_of_favorites_books().count(title) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        title = 'Преступление и наказание'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)
        collector.delete_book_from_favorites(title)

        assert title not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        title = 'Капитанская дочка'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)

        assert collector.get_list_of_favorites_books() == [title]
