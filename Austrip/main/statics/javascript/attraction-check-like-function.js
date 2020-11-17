var script = document.createElement('script');
script.src = '//code.jquery.com/jquery-1.11.0.min.js';

document.getElementsByTagName('head')[0].appendChild(script);

let likeBtn = document.getElementById("like-button")

window.onload = function () {
    checkLikes()
    checkDislikes()
}

function checkLikes() {
    $.ajax({
        type: 'GET',
        url: 'checkLike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            if (data.toString() === "1") {
                likeBtn.style.color = "#008000"
            } else {
                likeBtn.style.color = "#a9a9a9"
            }
        },
        error: function (xhr, errmsg, err) {

        }
    });
}

function checkDislikes() {
    $.ajax({
        type: 'GET',
        url: 'checkDislike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            if (data.toString() === "0") {
                dislikeBtn.style.color = "#a9a9a9"
            } else {
                dislikeBtn.style.color = "#ff0000"
            }
        },
        error: function (xhr, errmsg, err) {

        }
    });
}

likeBtn.addEventListener("click", () => {
    $.ajax({
        type: 'GET',
        url: 'checkLike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            if (data.toString() === "0") {
                likeBtn.style.color = "#008000"
            } else {
                likeBtn.style.color = "#a9a9a9"
            }
        },
        error: function (xhr, errmsg, err) {

        }
    });
})
let dislikeBtn = document.getElementById("dislike-button")
dislikeBtn.addEventListener("click", () => {
    $.ajax({
        type: 'GET',
        url: 'checkDislike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            if (data.toString() === "1") {
                dislikeBtn.style.color = "#a9a9a9"
            } else {
                dislikeBtn.style.color = "#ff0000"
            }
        },
        error: function (xhr, errmsg, err) {

        }
    });
})
