let bookmarkBtn = document.querySelector('#bookmarkBtn');
var bookmarked = false;
document.getElementById("bookmarkBtn").style.color="#a9a9a9";
bookmarkBtn.addEventListener('click',()=>{
    if(bookmarked){
        bookmarked=false;
        document.getElementById("bookmarkBtn").style.color="#a9a9a9";
    }
    else{
        bookmarked=true;
        document.getElementById("bookmarkBtn").style.color="#daa520";
    }
})