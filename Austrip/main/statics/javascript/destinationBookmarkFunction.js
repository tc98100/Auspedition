let bookmarkBtn =document.getElementById("dBookBtn")
        let bookmarked = false;
        bookmarkBtn.style.color="#a9a9a9";
        bookmarkBtn.addEventListener('click',()=>{
            if(bookmarked){
                bookmarked=false;
                bookmarkBtn.style.color=bookmarked?"#daa520":"#a9a9a9";

            }
            else{
                bookmarked=true;
                bookmarkBtn.style.color=bookmarked?"#daa520":"#a9a9a9";
            }
        })