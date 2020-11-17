var script = document.createElement('script');

script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let attractionLikeBtn = document.getElementById("like-button")
let attractionLikeCount = document.getElementById("like-count")


attractionLikeBtn.addEventListener('click', () => {
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

        }
    });
})

let attractionDislikeBtn = document.getElementById("dislike-button")
let attractionDislikeCount = document.getElementById("dislikeCount")


attractionDislikeBtn.addEventListener('click', () => {
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

        }
    });
})