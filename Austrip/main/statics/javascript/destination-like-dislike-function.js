var script = document.createElement('script');
script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let destinationLikeBtn = document.getElementById("d-like-btn")
let destinationLikeCount = document.getElementById("d-like-count")


destinationLikeBtn.addEventListener('click', () => {
    alert("loading likes")
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

        }
    });
})

let destinationDislikeBtn = document.getElementById("d-dislike-btn")
let destinationDislikeCount = document.getElementById("d-dislike-count")

destinationDislikeBtn.addEventListener('click', () => {
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

        }
    });
})