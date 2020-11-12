let container = document.getElementById("comments");
let btn = document.getElementById("loadMoreBtn");
btn.addEventListener('click',()=>{
    loadComments(3)
})

function loadComments(numberOfComments){
    var comments="";
    for(i=0;i<numberOfComments;i++){
        comments+="<div class=\"container comment  m-1 p-0\">\n" +
        "            <div class=\" ml-3 border-left \">\n" +
        "                <div class=\"container ml-2\">\n" +
        "                    <a class=\"author\">\n" +
        "                        <span>User"+i+"</span>\n" +
        "                        <span class=\"summary-text small\">time stamp to be added</span>\n" +
        "                    </a>\n" +
        "                </div>\n" +
        "                <div class=\"messageText ml-2 container m-2\">Actual comments to be pulled from db</div>\n" +
        "            </div>\n" +
        "        </div>";
    }
    container.insertAdjacentHTML("beforeend",comments);
}