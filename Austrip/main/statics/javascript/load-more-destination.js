var script = document.createElement('script');

script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let destinations = document.getElementById("destinations")
         let btn = document.getElementById("loadDestinationBtn")
        let cards =""
        let count = 4;
          btn.addEventListener("click",()=>{
              alert("Loading in progress,Please wait for 2 seconds.")
              cards=""
            $.ajax({
                method: "GET",
                 url: "http://127.0.0.1:8000/viewset/destination/",
                 success: function (response) {
                    cards += "<div class=\"row justify-content-between\">\n"
                     for(let i =count;i<count+3;i++){
                         if(i>=response.length){
                            alert("All content loaded.")
                             break;
                         }
                     let link = "/destinations/"+response[i].destination_id+"/"
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
            "                                    <a class=\"btn btn-success my-2\" href="+link+">see more</a>\n" +
            "                                </div>\n" +
            "                            </div>\n" +
            "                        </div>\n" +
            "                    </div>\n" +
            "                </div>";

                 }
                 cards += "</div>"
                     if(count-1>=response.length){
                         cards=""
                     }
                     destinations.insertAdjacentHTML("beforeend", cards);
                     count+=3;
                 }

            })
        });