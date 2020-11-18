let LoadCommentBtn = document.getElementById("aLoadMoreBtn")
let aComments = document.getElementById("aComments")
let cards = ""
let count = 4;
LoadCommentBtn.addEventListener("click", () => {
    alert("Loading in progress,Please wait for 2 seconds.")
    cards = ""
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:8000/viewset/attractionComment/?comment_on=" + LoadCommentBtn.value,
        success: function (response) {
            cards += "<div class=\"row\">\n"
            for (let i = count; i < count + 3; i++) {
                if (i >= response.length) {
                    alert("All content loaded.")
                    break;
                }
                let dateObject = new Date(response[i].created_time)
                const date = dateObject.toLocaleString()

                cards += " <div class=\"container comment  m-1 p-0\">\n" +
                    "                    <div class=\" ml-3 border-left \">\n" +
                    "                        <div class=\"container ml-2\">\n" +
                    "                            <a class=\"author\">\n" +
                    "                                <span>User# " + response[i].user + "</span>\n" +
                    "                                <span class=\"summary-text small\">" + date + "</span>\n" +
                    "                            </a>\n" +
                    "                        </div>\n" +
                    "                        <div class=\"messageText ml-2 container m-2\">" + response[i].comment_content + "</div>\n" +
                    "                    </div>\n" +
                    "                </div>";

            }
            cards += "</div>"
            if (count - 1 >= response.length) {
                cards = ""
            }
            aComments.insertAdjacentHTML("beforeend", cards);
            count += 3;
        }

    })
});