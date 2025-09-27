# Books Collector - тесты

---

## Реализованные тесты:

- `test_add_new_book_add_two_books`: добавление двух книг
- `test_add_new_book_name_length_40_or_less`: параметризованный тест на длину имени <= 40
- `test_add_new_book_name_too_long`: имя больше 40 символов не добавляется
- `test_add_new_book_duplicate`: нельзя добавить одну и ту же книгу дважды
- `test_set_book_genre_success`: параметризованный тест на установку жанра из списка
- `test_set_book_genre_not_in_genre_list`: нельзя установить невалидный жанр
- `test_set_book_genre_for_nonexistent_book`: нельзя установить жанр несуществующей книге
- `test_get_books_with_specific_genre`: получить список книг с определённым жанром
- `test_get_books_with_specific_genre_no_books`: если книг с жанром нет, то пустой список
- `test_get_books_genre`: возвращается словарь книг и жанров
- `test_get_books_for_children_filters_age_rating`: книги с возрастным рейтингом не попадают в список для детей
- `test_add_book_in_favorites_success`: добавить книгу в избранное
- `test_add_book_in_favorites_nonexistent_book`: нельзя добавить несуществующую книгу в избранное
- `test_add_book_in_favorites_twice`: нельзя добавить в избранное дважды
- `test_delete_book_from_favorites`: удалить книгу из избранного
- `test_get_list_of_favorites_books`: возвращается список избранных книг
