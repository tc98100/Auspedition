var script = document.createElement('script');

script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let attraction = document.getElementById("attractions")
let btn = document.getElementById("loadAttractionBtn")
let count = 4;
btn.addEventListener("click", () => {
    let cards = ""
    alert("Loading in progress,Please wait for a while.")
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:8000/viewset/attraction/",
        success: function (response) {
            let length = response.length
            cards += "<div class=\"row\">\n"
            for (let i = count; i < count + 4; i++) {
                if (i >= length) {
                    alert("All content loaded.")
                    break;
                }
                let link = "/attractions/" + response[i].attraction_id + "/"
                cards += "<div class=\"col-3 mb-2\">\n" +
                "                    <div class=\"card rounded-cus shadow\">\n" +
                "                        <a class=\"attraction\" style=\"background-image: url(" + response[i].image + "); display: block\"></a>\n" +
                "                        <div class=\"card-body\">\n" +
                "                            <p class=\"font-weight-bold text-center\"\n" +
                "                               style=\"font-size: 1.1rem; line-height: 1rem\">" + response[i].name + "</p>\n" +
                "                            <hr>\n" +
                "                            <div class=\"row text-center\">\n" +
                "                                <div class=\"col\">\n" +
                "                                    <p class=\"\"><b>" + response[i].likes + "</b> likes</p>\n" +
                "                                    <p><b>" + response[i].dislikes + "</b> dislikes</p>\n" +
                "                                </div>\n" +
                "                                <div class=\"col\">\n" +
                "                                    <a class=\"btn btn-success my-2\"\n" +
                "                                       href=" + link + ">see more</a>\n" +
                "                                </div>\n" +
                "                            </div>\n" +
                "                        </div>\n" +
                "                    </div>\n" +
                "                </div>";
            }
            cards += "</div>"
            if (count - 1 >= response.length) {
                cards = ""
            }
            attraction.insertAdjacentHTML("beforeend", cards);
            count += 4;
        }

    })
});