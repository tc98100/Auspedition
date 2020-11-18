var script = document.createElement('script');
script.src = '//code.jquery.com/jquery-1.11.0.min.js';

document.getElementsByTagName('head')[0].appendChild(script);

window.addEventListener("load", checkLikes, false);
window.addEventListener("load", checkDislikes, false);

let attractionLikeBtn = document.getElementById("like-button")
let attractionLikeCount = document.getElementById("like-count")

let attractionDislikeBtn = document.getElementById("dislike-button")
let attractionDislikeCount = document.getElementById("dislikeCount")

function checkLikes() {
    $.ajax({
        type: 'GET',
        url: 'checkLike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            attractionLikeBtn.style.color = data
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
            attractionDislikeBtn.style.color = data
        },
        error: function (xhr, errmsg, err) {
        }
    });
}


attractionLikeBtn.addEventListener('click', () => {
    alert("Like button clicked, data update process may be slow.")
    $.ajax({
        type: 'POST',
        url: 'like/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            attractionLikeCount.innerHTML = data
        },
        error: function (xhr, errmsg, err) {

        },
        complete: function (response) {
            checkLikes()
        }
    });
})
attractionDislikeBtn.addEventListener('click', () => {
    alert("Dislike button clicked, data update process may be slow")
    $.ajax({
        type: 'POST',
        url: 'dislike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            attractionDislikeCount.innerHTML = data

        },
        error: function (xhr, errmsg, err) {

        },
        complete: function (response) {
            checkDislikes()
        }

    })
});