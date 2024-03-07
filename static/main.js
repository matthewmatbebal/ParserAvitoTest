// Функция для выполнения GET-запроса
function getData() {
    let link_psrsm = "https://www.avito.ru/krasnodar/doma_dachi_kottedzhi/prodam/dom-ASgBAQICAUSUA9AQAUDYCBTOWQ?localPriority=0&map=eyJzZWFyY2hBcmVhIjp7ImxhdEJvdHRvbSI6NDUuMDM2NTMwMjM2MjY5ODU0LCJsYXRUb3AiOjQ1LjA0MjMyOTg2MTk2ODIsImxvbkxlZnQiOjM5LjAwOTMxMzYxNjM0ODIxNiwibG9uUmlnaHQiOjM5LjAyNDU0ODU2MzU1Mjh9LCJ6b29tIjoxN30%3D"

    const url = '/getData'

    const params = {
        method: 'POST', // Указываем метод запроса (GET, POST и т. д.)
        headers: {
            'Content-Type': 'application/json' // Указываем тип содержимого
        },
        body: JSON.stringify({ link: link_psrsm }) // Преобразуем параметры в JSON и передаем в теле запроса
    };

    fetch(url, params) // Отправляем GET-запрос к /getData
        .then(response => response.json()) // Преобразуем полученный ответ в JSON
        .then(data => {
            // Обрабатываем полученные данные
            console.log(data); // Выводим данные в консоль (можно изменить на нужное действие)
            // Например, можно добавить код для отображения данных в виде таблицы на странице
            displayData(data); // Вызываем функцию для отображения данных на странице
        })
        .catch(error => {
            console.error('Error fetching data:', error); // Выводим сообщение об ошибке в консоль
        });
}

// Функция для отображения данных на странице
function displayData(data) {
    // Находим элемент, в котором будем отображать данные
    const dataContainer = document.getElementById('dataContainer');
    // Очищаем содержимое элемента перед отображением новых данных
    dataContainer.innerHTML = '';

    // Создаем элементы для отображения данных (например, таблицу)
    const table = document.createElement('table');
    const tbody = document.createElement('tbody');

    // Проходимся по полученным данным и создаем строки таблицы
    data.forEach(item => {
        const row = document.createElement('tr');
        const linkCell = document.createElement('td');
        linkCell.textContent = item.link;
        const priceCell = document.createElement('td');
        priceCell.textContent = item.price;
        const nameCell = document.createElement('td');
        nameCell.textContent = item.name;

        // Добавляем ячейки в строку
        row.appendChild(linkCell);
        row.appendChild(priceCell);
        row.appendChild(nameCell);

        // Добавляем строку в тело таблицы
        tbody.appendChild(row);
    });

    // Добавляем тело таблицы в таблицу
    table.appendChild(tbody);

    // Добавляем таблицу в контейнер для данных
    dataContainer.appendChild(table);
}