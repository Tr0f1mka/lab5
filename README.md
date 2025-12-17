<h1>Лабораторная работа №5 "Работа с отладчиком"</h1>
<hr>
<p>Отладка кодовой базы лабораторной работы №4 с помощью средств отладки.</p>
<hr>

<h2>Важные файлы/папки</h2>
<ul>
    <li>README.md - отчёт по работе</li>
    <li>src - исправленная версия проекта. В этой директории можно найти места, в которых были баги(поиск по слову "Баг").</li>
    <li>src buggy - неисправленная версия проекта</li>
</ul>


<hr>
<h2>Отчёт</h2>
<h3>Ошибка 1 — взятие не метода как метод</h3>

<p>Место: base_classes.py, класс Goose, метод __add__</p>

<p>Симптом:
Попытка взять поле target(класс Player) как метод класса Goose.</p>

<p>Как воспроизвести:
Запустить симуляцию с seed=1.</p>

<p>Отладка:
Установлен breakpoint на строки «methods[component] = getattr(self, component).__func__». 
В отладчике видно, что программа пытается взять «target» как метод класса Goose.</p>

<p>Причина:
Отсутствует «отсеивание» target при сборе методов слагаемых гусей.</p>

<p>Исправление:</p>
<p>Добавлено:</p>
```python
if component == "target":
	continue
```

<p>Проверка:
Поведение симуляции соответствует ожидаемому.</p>

<p>Доказательства:
    <ul>
        <li>screens/bug1/place_with_exception.png</li>
        <li>screens/bug1/locals.png</li>
    </ul>
</p>

<h3>Ошибка 2 — использование игрока-цели как метод</h3>

<p>Место: player_collection.py, класс PlayerCollection, метод honk_update.</p>

<p>Симптом:
Отрицательный cчёт игроков в конце.</p>

<p>Как воспроизвести:
Запустить симуляцию с seed=4 и steps=60.</p>

<p>Отладка:
Установлен breakpoint на строке «i.balance -= 5».
В отладчике видно, что программа пытается взять «target» как метод класса Goose.</p>

<p>Причина:
Отсутствует «отсеивание» target при сборе методов слагаемых гусей.</p>

<p>Исправление:
    Добавлено:
    ```python
    if component == "target":
        continue
    ```
</p>

<p>Проверка:
Поведение симуляции соответствует ожидаемому.</p>

<p>Доказательства:
    <ul>
        <li>screens/bug2/place_where_bug_is_visible.png</li>
        <li>screens/bug2/locals.png</li>
    </ul>
<p>

<h3>Ошибка 3 — кража игроком несуществующих монет</h3>

<p>Место: players.py, класс LuckPlayer, метод steel_goose.</p>

<p>Симптом:
Отрицательный cчёт у обворовываемого гуся.</p>

<p>Как воспроизвести:
Запустить симуляцию с seed=4.</p>

<p>Отладка:
Установлен breakpoint на строке «self.balance += s».
В отладчике видно, что баланс гуся становится отрицательным.</p>

<p>Причина:
Отсутствует проверка наличия воруемой у гуся суммы.</p>

<p>Исправление:
    Изменено:
    ```python
    if s <= goose.balance:
        	goose.balance -= s
        	self.balance += s
        print(f"Ловкий игрок {self.name} успешно крадёт у гуся {goose.name} {s} монет")

    else:
     	self.balance += goose.balance
             print(f"Ловкий игрок {self.name} успешно крадёт у гуся {goose.name} {goose.balance} монет")
             goose.balance = 0
    ```
</p>

<p>Проверка:
Поведение симуляции соответствует ожидаемому.</p>

<p>Доказательства:
    <ul>
        <li>screens/bug3/place_where_bug_is_visible.png</li>
        <li>screens/bug3/locals.png</li>
    </ul>
</p>

<h3>Ошибка 4 — использование гуся-кредитора как метод</h3>

<p>Место: base_place.py, класс Player, метод __call__.</p>

<p>Симптом:
Симуляция пытается вызвать гуся-кредитора во время вызова метода игрока.</p>

<p>Как воспроизвести:
Запустить симуляцию с seed=14 и steps=50.</p>

<p>Отладка:
Установлен breakpoint на строке «method(players.random())».
В отладчике видно, что программа пытается выполнить «creditor» как метод класса Player.</p>

<p>Причина:
Отсутствует «отсеивание» creditor при сборе методов слагаемых гусей.</p>

<p>Исправление:
    Добавлено:
    ```python
    if component == "creditor":
    	continue
    ```
</p>

<p>Проверка:
Поведение симуляции соответствует ожидаемому.</p>

<p>Доказательства:
    <ul>
        <li>screens/bug4/place_where_bug_is_visible.png</li>
        <li>screens/bug4/locals.png</li>
    </ul>
</p>

<h3>Ошибка 5 — удаление игрока из пустой коллекции</h3>

<p>Место: casino.py, класс Casino, метод iteration.</p>

<p>Симптом:
Повторные срабатывания метода repress стаи, в которой есть BouncerGoose, вызывает исключение взятия игрока из пустой коллекции.</p>

<p>Как воспроизвести:
Запустить симуляцию с seed=2 и steps=40.</p>

<p>Отладка:
Установлен breakpoint на строке «result = goose(self.players, self.geese)».
В отладчике видно, что программа передаёт пустую коллекцию игроков как аргумент метода __call__ экземпляра класса Goose.</p>

<p>Причина:
Отсутствует проверка пустоты коллекции игроков в цикле методов гусей.</p>

<p>Исправление:
    Добавлено:
    ```python
    if not self.players:
        self.goose_balance.update_balance(self.geese)
            self.player_balance.update_balance(self.players)
            return
    ```
</p>

<p>Проверка:
Поведение симуляции соответствует ожидаемому.</p>

<p>Доказательства:
    <ul>
        <li>screens/bug5/place_where_bug_is_visible.png</li>
        <li>screens/bug5/locals.png</li>
    </ul>
</p>