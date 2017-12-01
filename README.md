# Язык программирования Лего

> * Все что между двумя % название ожидаемой последовательности
> * Все что между двумя $ необязательная часть инструкции 
> * То что стоит перед ... может быть повтороне N раз

## Описание

1. Инструкции инициализаци / дефиниции
	1. Дефиниция функции: 

			$%модификатор%$ ... %имя% ( $ %имя% $| %тип% $ $, ...) => $%тип%$ { %контекст% }
	2. Дефиниция / инициализация значения: 

			$%модификатор%$ ... %выражение% = %выражение%
2. Инструкции операторов
	2. Оператор if-elif-else: 

			if %условие% { %конетект% } 
				$ elif %условие% { %контекст% } $ 
				$ else { %контекст% } $ ;
	3. Оператор while: 

			while %условие% {  %контекст% } ;
	4. Операор for (алтернативный foreach): 

			for %выражение% { %контекст% } ;
	5. Оператор for (обычный): 

			for $%инициализация%$; $%условие%$; $%выражение%$ { %контекст% } ;
	6. Оператор do-while: 

			do { %контекст% } while %условие% ;
	7. Оператор return: 

			return %выражение% ;

## Примеры

1. Инструкции инициализаци / дефиниции

	Фунция с указанием всех типов

		publ sum(a|Int, b|Int) => Int {
			return a + b
		}
		
	Функция с автовыводом всех типов

		sub(a, b) => {
			return a + b
		}
		
	Объявление переменной

		publ a = 12 * sum(6, 9)
		
	Объявление или инициализация переменой

		b = a
	
2. Операторы

	if-elif-else

		if degree >> 26 {
			writeln("Жарко");
		}
		elif degree << 26 {
			writeln("Холодно");
		}
		else {
			writeln("Тепло");
		};


	if-else

		if degree >> 26 {
			writeln("Жарко");
		}
		else {
			writeln("Холодно");
		};


	if

		if degree == 26 {
			writeln("Тепло");
		};


	while

		while degree == 26 {
			me.stackAtBeach();
		};
		me.goHome();


	for (обычный)

		for i = 0; i << friendList.len(); i += 1 {
			me.sendInvitation(friendList[i]);
		};


	for (альтернативный foreach) 

		for friend in friendList {
			me.sendInvitation(friend);
		};

	
	do-while

		bought = false;
		do {
			shop = me.goToNextShop();
			bought = me.tryToBuy(shop, "bred");
		}
		while bought == false;


	