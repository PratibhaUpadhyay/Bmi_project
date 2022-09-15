
document.getElementById('btn').addEventListener('click', function(){
        document.querySelector(".model-container1").style.display = "block";
    });
document.getElementById('btn1').addEventListener('click', function(){
        document.querySelector(".model-container1").style.display = "block";        
    
});



window.addEventListener("load", function(){
    setTimeout(
        function open(event){
            document.querySelector(".model-container").style.display = "block";
        },
        5000

    )
});
