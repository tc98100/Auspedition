let attraction = document.getElementById("attractions")
let btn = document.getElementById("loadAttractionBtn")
let cards =""
let count = 4;
          btn.addEventListener("click",()=>{
            $.ajax({
                method: "GET",
                 url: "http://127.0.0.1:8000/viewset/attraction/",
                 success: function (response) {
                    let length = response.length
                    cards += "<div style=\"padding-top: 25px\">"
                    cards += "<div class=\"row justify-content-between\">\n"
                     for(let i =0;i<count+3;i++){
                         console.log("i is "+i)
                         console.log("length is "+length)
                         if(i>=length){

                             break;
                         }
                     console.log(response[i].attraction_id)
                      cards += "<div class=\"col-3 mb-2\">\n" +
            "                    <div class=\"card rounded-cus shadow\">\n" +
            "                        <a class=\"attraction\" style=\"background-image: url(" + response[i].image + "); display: block\"></a>\n" +
            "                        <div class=\"card-body\">\n" +
            "                            <p class=\"font-weight-bold text-center\" style=\"font-size: 1.5rem; line-height: 1rem\">" + response[i].name + "</p>\n" +
            "                            <hr>\n" +
            "                            <div class=\"row text-center\">\n" +
            "                                <div class=\"col\">\n" +
            "                                    <p class=\"\">" + response[i].likes + " people liked it</p>\n" +
            "                                    <p>" + response[i].dislikes + " people disliked it</p>\n" +
            "                                </div>\n" +
            "                                <div class=\"col\">\n" +
            "                                    <a class=\"btn btn-success my-2\" href=\"{% url 'attraction_details' attraction=" + response[i].attraction_id + " %}\">see more</a>\n" +
            "                                </div>\n" +
            "                            </div>\n" +
            "                        </div>\n" +
            "                    </div>\n" +
            "                </div>";

                 }
                 cards += "</div>"
                cards += "</div>"
                     attraction.insertAdjacentHTML("beforeend", cards);
                     count+=3;
                 }

            })
        });
