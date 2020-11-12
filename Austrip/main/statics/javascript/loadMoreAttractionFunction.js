let attraction = document.getElementById("attractions")
let btn = document.getElementById("moreBtn")
btn.addEventListener("click",()=>{
    loadMore();
});
function loadMore(){
    var cards="";
    cards+="<div style=\"padding-top: 25px\">"
    cards+="<div class=\"row justify-content-between\">\n"
    for(i=0;i<3;i++){
        cards+="<div class=\"col-4 \">\n" +
            "                    <div class=\"card rounded-cus\">\n" +
            "                        <div class=\"attraction\" style=\"background-image: url({% static 'AyersMountain.jpg'%});\">\n" +
            "                        </div>\n" +
            "                        <div class=\"card-body card-body-attraction\">\n" +
            "                            <p class=\"font-weight-bold text-center\">Ayers Mountain</p>\n" +
            "                        </div>\n" +
            "                    </div>\n" +
            "                </div>";
    }
    cards+="</div>"
    cards+="</div>"
    attraction.insertAdjacentHTML("beforeend",cards);
};