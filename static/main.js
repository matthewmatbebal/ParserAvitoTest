function getData() {
    const spinner = document.getElementById('spinner');
    spinner.classList.remove("hidden")


    let inputValue = document.getElementById('input-link').value;
    let xhr = new XMLHttpRequest();

    xhr.open("POST", "http://localhost:5000/getData", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          let response = JSON.parse(xhr.responseText);
          displayData(response)
          spinner.classList.add("hidden")
        } else {
          console.error('Request failed: ' + xhr.status);
        }
      }
    };

    let data = {
        link: inputValue,
    };

    xhr.send(JSON.stringify(data))
}

function displayData(data) {
    const dataContainer = document.getElementById('tbody');
    dataContainer.innerHTML = '';

    data.forEach(item => {
        const row = document.createElement('tr');

        const idCell = document.createElement('th');
        idCell.textContent = item.id;

        const linkCell = document.createElement('td');
        linkCell.innerHTML = '<a href="' + item.link + '"> Link to AD </a>';

        const squareField = document.createElement('td');
        squareField.textContent = item.square_field;

        const squareHouse = document.createElement('td');
        squareHouse.textContent = item.square_house;

        const price = document.createElement('td');
        price.textContent = item.price;

        const price_per_meter = document.createElement('td');
        price_per_meter.textContent = item.price_per_meter;

        const phone = document.createElement('td');
        phone.textContent = item.phone;

        const views_count = document.createElement('td');
        views_count.textContent = item.views_count;

        row.appendChild(idCell);
        row.appendChild(linkCell);
        row.appendChild(squareField);
        row.appendChild(squareHouse);
        row.appendChild(price);
        row.appendChild(price_per_meter);
        row.appendChild(phone);
        row.appendChild(views_count);

        dataContainer.appendChild(row);
    });
}