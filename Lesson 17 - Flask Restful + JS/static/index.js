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

const targetElement = document.getElementById("cards");

fetch("/api/articles")
    .then(response => response.json())
    .then(articles => {
        articles.forEach(article => {
            
            const card = document.createElement("div");
            card.className = "card";
            card.style = "width: 18rem;"

            const cardElement = document.createElement("div");
            cardElement.className = "card-body";

            const titleElement = document.createElement("h5");
            titleElement.className = "card-title";
            titleElement.id = "card_title";
            titleElement.textContent = article.title;
            cardElement.appendChild(titleElement);

            const dateElement = document.createElement("h6");
            dateElement.className = "card-subtitle mb-2 text-body-secondary";
            dateElement.id = "card_date";
            dateElement.textContent = article.date;
            cardElement.appendChild(dateElement);
            
            const bodyElement = document.createElement("p");
            bodyElement.className = "card-text";
            bodyElement.id = "card_body";
            bodyElement.textContent = article.body;
            cardElement.appendChild(bodyElement);
            
            const deleteLinkElement = document.createElement("a");
            deleteLinkElement.href = "/article/" + article.id + "/delete";
            deleteLinkElement.className = "card-link";
            deleteLinkElement.textContent = "Delete";
            cardElement.appendChild(deleteLinkElement);

            card.appendChild(cardElement)
            targetElement.appendChild(card);
        });
    })
    .catch(error => {
        console.error("Error fetching articles data:", error);
    });
