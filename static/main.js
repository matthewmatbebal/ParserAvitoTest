function getData() {
    let link_psrsm = "test"
    let xhr = new XMLHttpRequest();

    xhr.open("POST", "http://localhost:5000/getData", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    let data = {
        link: link_psrsm,
    };

    xhr.send(JSON.stringify(data));
}

function displayData(data) {
    const dataContainer = document.getElementById('dataContainer');
    dataContainer.innerHTML = '';

    const table = document.createElement('table');
    const tbody = document.createElement('tbody');

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