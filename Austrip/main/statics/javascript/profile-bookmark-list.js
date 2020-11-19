let script = document.createElement('script');

script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);
window.onload = function () {
    loadAttractionBookmark()
    loadDestinationBookmark()
}

function loadAttractionBookmark() {
    let cards = document.getElementById("a-book-cards")
    let texts = ""
    $.ajax({
        method: "GET",
        url: "abookmark/",
        success: function (data) {
            obj = JSON.parse(JSON.stringify(data))
            for (let i = 0; i < data.length; i++) {
                texts = ""
                let link = "/attractions/" + obj[i].attraction_id + "/"
                let attractionId = obj[i].attraction_id
                let cardId = attractionId + "_card"
                let buttonId = attractionId + "_button"
                texts += "<div class=\"card\" id=\"" + cardId + "\">\n" +
                    "                            <a class=\"attraction\" style=\"background-image: url(http://127.0.0.1:8000/assets/"+obj[i].image+"); display: block\"></a>\n" +
                    "                    <div class=\"card-body\" style=\"text-align:center\">\n" +
                    "                        <h5 class=\"card-title\">" + obj[i].name + "</h5>\n" +
                    "                        <div class=\"bookmarkBtnGroup\">\n" +
                    "                        <a href=" + link + " class=\"btn btn-success btn-sm btn-block\">Go To This Page</a>\n" +
                    "                        <button id=\"" + buttonId + "\" class=\"btn btn-danger mr-4 btn-sm btn-block\">Remove Bookmark</button>`\n" +
                    "                        </div>\n" +
                    "                    </div>\n" +
                    "                </div>"
                cards.insertAdjacentHTML("beforeend", texts)
                document.getElementById(buttonId).addEventListener("click", () => {
                    removeAttractionBookmark(attractionId)
                    document.getElementById(cardId).remove()
                })
            }
        },
        error() {
            alert("Error In bookmark data")
        }
    })
}

function removeAttractionBookmark(id) {
    let cards = document.getElementById(id + "_card")
    $.ajax({
        type: 'POST',
        url: "/attractions/" + id + "/bookmark/",
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
    });
}

function loadDestinationBookmark() {
    let cards = document.getElementById("d-book-cards")
    let texts = ""
    $.ajax({
        method: "GET",
        url: "dbookmark/",
        success: function (data) {
            obj = JSON.parse(JSON.stringify(data))
            for (let i = 0; i < data.length; i++) {
                texts = ""
                let link = "/destinations/" + obj[i].destination_id + '/'
                let destinationId = obj[i].destination_id
                let cardId = destinationId + "_card"
                let buttonId = destinationId + "_button"
                texts += "<div class=\"card\" id=\"" + cardId + "\">\n" +
                    "                            <a class=\"attraction\" style=\"background-image: url(http://127.0.0.1:8000/assets/"+obj[i].image+"); display: block\"></a>\n" +
                    "                    <div class=\"card-body\" style=\"text-align:center\">\n" +
                    "                        <h5 class=\"card-title\">" + obj[i].name + "</h5>\n" +
                    "                        <div class=\"bookmarkBtnGroup\">\n" +
                    "                        <a href=" + link + " class=\"btn btn-success btn-sm btn-block\">Go To This Page</a>\n" +
                    "                        <button id=\"" + buttonId + "\" class=\"btn btn-danger mr-4 btn-sm btn-block\">Remove Bookmark</button>`\n" +
                    "                        </div>\n" +
                    "                    </div>\n" +
                    "                </div>"
                 cards.insertAdjacentHTML("beforeend", texts)
                document.getElementById(buttonId).addEventListener("click", () => {
                    removeDestinationBookmark(destinationId)
                    document.getElementById(cardId).remove()
                })
            }

        },
        error() {
            alert("Error In bookmark data")
        }
    })
}
function removeDestinationBookmark(id) {
    let cards = document.getElementById(id + "_card")
    $.ajax({
        type: 'POST',
        url: "/destinations/" + id + "/bookmark/",
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
    });
}