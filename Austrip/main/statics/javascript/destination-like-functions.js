var script = document.createElement('script');
script.src = '//code.jquery.com/jquery-1.11.0.min.js';

document.getElementsByTagName('head')[0].appendChild(script);

window.addEventListener("load", checkLikes, false);
window.addEventListener("load", checkDislikes, false);

let destinationLikeBtn = document.getElementById("d-like-btn")
let destinationLikeCount = document.getElementById("d-like-count")

let destinationDislikeBtn = document.getElementById("d-dislike-btn")
let destinationDislikeCount = document.getElementById("d-dislike-count")

function checkLikes() {
    $.ajax({
        type: 'GET',
        url: 'checkLike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            destinationLikeBtn.style.color = data
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
            destinationDislikeBtn.style.color = data
        },
        error: function (xhr, errmsg, err) {
        }
    });
}


destinationLikeBtn.addEventListener('click', () => {
    alert("Like button clicked, data update process may be slow.")
    $.ajax({
        type: 'POST',
        url: 'like/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            destinationLikeCount.innerHTML = data
        },
        error: function (xhr, errmsg, err) {

        },
        complete: function (response) {
            checkLikes()
        }
    });
})
destinationDislikeBtn.addEventListener('click', () => {
    alert("Dislike button clicked, data update process may be slow")
    $.ajax({
        type: 'POST',
        url: 'dislike/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            destinationDislikeCount.innerHTML = data

        },
        error: function (xhr, errmsg, err) {

        },
        complete: function (response) {
            checkDislikes()
        }

    })
});