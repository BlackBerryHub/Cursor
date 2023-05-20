fetch("/api/menu-items")
    .then(response => response.json())
    .then(function (response) {
        var menu = document.getElementById("menu")
        for (let el of response) {
            var li = document.createElement("li");
            li.classList.add("nav-item");
            li.innerHTML = "<a href='" + el.link + "' class='nav-link'>" + el.name + "</a>";
            menu.append(li);
        }
    })

// Assuming you have a target element to append the HTML
const targetElement = document.getElementById("cards");

// Make a fetch request to retrieve the articles data
fetch("/api/articles")
    .then(response => response.json())
    .then(articles => {
        // Loop through each article
        articles.forEach(article => {
            // Create the card element
            const card = document.createElement("div");
            card.className = "card";
            card.style = "width: 18rem;"

            const cardElement = document.createElement("div");
            cardElement.className = "card-body";

            // Create the card title element
            const titleElement = document.createElement("h5");
            titleElement.className = "card-title";
            titleElement.id = "card_title";
            titleElement.textContent = article.title;
            cardElement.appendChild(titleElement);

            // Create the card date element
            const dateElement = document.createElement("h6");
            dateElement.className = "card-subtitle mb-2 text-body-secondary";
            dateElement.id = "card_date";
            dateElement.textContent = article.date;
            cardElement.appendChild(dateElement);

            // Create the card body element
            const bodyElement = document.createElement("p");
            bodyElement.className = "card-text";
            bodyElement.id = "card_body";
            bodyElement.textContent = article.body;
            cardElement.appendChild(bodyElement);

            // Create the delete link element
            const deleteLinkElement = document.createElement("a");
            deleteLinkElement.href = "/article/" + article.id + "/delete";
            deleteLinkElement.className = "card-link";
            deleteLinkElement.textContent = "Delete";
            cardElement.appendChild(deleteLinkElement);

            // Append the card element to the target element
            card.appendChild(cardElement)
            targetElement.appendChild(card);
        });
    })
    .catch(error => {
        console.error("Error fetching articles data:", error);
    });
