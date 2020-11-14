let likeBtn = document.getElementById("likeBtn");
likeBtn.style.color="#a9a9a9"
let dislikeBtn = document.getElementById("dislikeBtn");
dislikeBtn.style.color="#a9a9a9"
let liked = false;
let disliked = false;
let likeCount= document.getElementById("likeCount").innerHTML;
let dislikeCount= document.getElementById("dislikeCount").innerHTML;

likeBtn.addEventListener('click',()=>{
    if(!liked) {
        liked = true;
        likeCount+=1;
    }
    if(disliked) {
        disliked = false
        dislikeCount-=1;
        likeCount+=1;

    }
    likeBtn.style.color=liked?"#008000":"#a9a9a9";
    dislikeBtn.style.color=disliked?"#ff0000":"#a9a9a9";

})
dislikeBtn.addEventListener('click',()=>{
    if(!disliked) {
        disliked = true;
    }
    if(liked) {
        liked = false
    }
    dislikeBtn.style.color=disliked?"#ff0000":"#a9a9a9";
    likeBtn.style.color=liked?"#008000":"#a9a9a9";

})