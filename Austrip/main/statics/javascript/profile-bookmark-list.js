let script = document.createElement('script');

script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);
window.onload = function () {
    loadAttractionBookmark()
    loadDestinationBookmark()
}

function loadAttractionBookmark() {
    cards = document.getElementById("a-book-cards")
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
                console.log(cardId)
                texts += "<div class=\"card\" id=\"" + cardId + "\">\n" +
                    "                    <img src=\"" + obj[i].image + "\" class=\"card-img-top\" alt=\"...\">\n" +
                    "                    <div class=\"card-body\" style=\"text-align:center\">\n" +
                    "                        <h5 class=\"card-title\">" + obj[i].name + "</h5>\n" +
                    "                        <div class=\"bookmarkBtnGroup\">\n" +
                    "                        <a href=" + link + " class=\"btn btn-success btn-sm btn-block\">Go To This Page</a>\n" +
                    "                        <button class=\"btn btn-danger mr-4 btn-sm btn-block\">Remove Bookmark</button>`\n" +
                    "                        </div>\n" +
                    "                    </div>\n" +
                    "                </div>"
                cards.insertAdjacentHTML("beforeend", texts)
                document.getElementById(cardId).addEventListener("click", () => {
                    loadPage(attractionId)
                })
            }
        },
        error() {
            alert("Error In bookmark data")
        }
    })
}

function loadPage(id) {
    let cards = document.getElementById(id + "_card")
    console.log(cards)
    $.ajax({
        type: 'POST',
        url: "/attractions/" + id + "/bookmark/",
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            location.reload()
        },
        error: function (xhr, errmsg, err) {
            location.reload()
        },
    });
}

function loadDestinationBookmark() {
    cards = document.getElementById("d-book-cards")
    let texts = ""
    $.ajax({
        method: "GET",
        url: "dbookmark/",
        success: function (data) {
            obj = JSON.parse(JSON.stringify(data))
            for (let i = 0; i < data.length; i++) {
                let link = "/destinations/" + obj[i].destination_id + '/'
                texts += "<div class=\"card\">\n" +
                    "                    <img src=\"" + obj[i].image + "\" class=\"card-img-top\" alt=\"...\">\n" +
                    "                    <div class=\"card-body\" style=\"text-align:center\">\n" +
                    "                        <h5 class=\"card-title\">" + obj[i].name + "</h5>\n" +
                    "                        <div class=\"bookmarkBtnGroup\">\n" +
                    "                        <a href=" + link + " class=\"btn btn-success btn-sm btn-block\">Go To This Page</a>\n" +
                    "                        <button class=\"btn btn-danger mr-4 btn-sm btn-block\">Remove Bookmark</button>`\n" +
                    "                        </div>\n" +
                    "                    </div>\n" +
                    "                </div>"
            }
            cards.insertAdjacentHTML("beforeend", texts)
        },
        error() {
            alert("Error In bookmark data")
        }
    })
}
