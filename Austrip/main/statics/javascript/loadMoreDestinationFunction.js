let destinations = document.getElementById("destinations")
let btn = document.getElementById("loadDestinationBtn")
btn.addEventListener("click",()=>{
    loadMore();
});
function loadMore(){
    var cards="";
    cards+="<div style=\"padding-top: 25px\">"
    cards+="<div class=\"row justify-content-between\">\n"
    for(i=0;i<4;i++){
        cards+="<div class=\"col-3 mb-2\">\n" +
            "                        <div class=\"card rounded-cus shadow\">\n" +
            "                            <a class=\"attraction\" style=\"background-image: url(https://www.sydneyoperahouse.com/content/dam/soh/footer/corporate/image-gallery/the-building/SOH_HL_2017_243_credit_HamiltonLund_1600x900.jpg); display: block\"></a>\n" +
            "                            <div class=\"card-body\">\n" +
            "                                <p class=\"font-weight-bold text-center\" style=\"font-size: 1.5rem; line-height: 1rem\">Sydney</p>\n" +
            "                                <hr>\n" +
            "                                <div class=\"row text-center\">\n" +
            "                                    <div class=\"col\">\n" +
            "                                        <p class=\"\">0 people liked it</p>\n" +
            "                                        <p>0 people disliked it</p>\n" +
            "                                    </div>\n" +
            "                                    <div class=\"col\">\n" +
            "                                        <a class=\"btn btn-success my-2\" >see more</a>\n" +
            "                                    </div>\n" +
            "                                </div>\n" +
            "                            </div>\n" +
            "                        </div>\n" +
            "                    </div>";
    }
    cards+="</div>"
    cards+="</div>"
    destinations.insertAdjacentHTML("beforeend",cards);
};