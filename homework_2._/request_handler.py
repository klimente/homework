""""Request handler"""

FRIENDS = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email@email.com'},
    {'name': 'Лолита', 'gender': 'Женский', 'sport': 'Бокс', 'email': 'email@email.com'},
    {'name': 'Джек', 'gender': 'Мужской', 'sport': 'Волейбол', 'email': 'email@email.com'}
]


def query(collection: list, select_func, *filters):
    """Main function which handle a query.

    :param collection: Collection to handle.
    :type name: str.
    :param select_func: Function that select fields in output collection.
    :type select_func: function.
    :param filters: Tuple of filters that filter the data in output collection.
    :type filters: function.
    :returns: list -- Output list of handler data or None.
    """
    query.coll = collection                    #создаю атрибут для работы остальных функций
    if collection:
        select_func()
        for filter in filters:
            filter()

    return list(query.coll)

def select(*field_name: str):
    """A function which returns function to work with fields data collection.

    :param field_name: Tuple of strings.
    :type field_name:str
    :returns: function -- To work with data of field_name or None.
    """
    def inner():
        """A function to work with fields that was defined in select function.

        :returns: None -- just change a mutable collection to output data.
        """
        if query.coll:
            for i in query.coll:
                for j in i.copy():
                    if j not in field_name:
                        i.pop(j)
        else:
            print("Коллекция не установлена")
    return inner

def field_filter(field_name: str, *collection: list):
    """A function to return function that filter a collection by fields.

    :param field_name: A name of field to filter.
    :type field_name: str.
    :param collection: Collection of values that must be in output data.
    :type collection: list.
    :returns: function -- that filter by parametr 'collection' or None.
    """
    def inner():
        """A function to work with fields and values that was defined in  fields_filter function.

        :returns: None -- change a mutable collection to output data.
        """
        if query.coll:
            for i in query.coll:
                for j in collection:
                    if i[field_name] not in j:
                        query.coll.pop(query.coll.index(i))
        else:
            print("Коллекция не установленна")
    return inner

C = query(
    FRIENDS,
    select("name", "gender", "sport"),
    field_filter('sport', ['Бокс', 'Волейбол']),
    field_filter('gender', ['Женский']),
    field_filter('name', ['Эмили'])
)

print(C)
