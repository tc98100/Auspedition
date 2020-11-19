
let destinationBookBtn = document.getElementById("d-bookmark-btn")
destinationBookBtn.addEventListener('click', () => {
    alert("Bookmark click, data update process may be slow.")
    $.ajax({
        type: 'POST',
        url: 'bookmark/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            destinationBookBtn.style.color = data
        },
        error: function (xhr, errmsg, err) {

        }, complete: function (response) {
            checkBookmark()
        }
    });
})


window.onload = function () {
    checkBookmark()
}

function checkBookmark() {
    $.ajax({
        type: 'GET',
        url: 'checkBookmark/',
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        success: function (data) {
            destinationBookBtn.style.color = data
        },
        error: function (xhr, errmsg, err) {

        }
    });
}
