// Show dialog window when option chosen

function filter(event){
    if (event.target.value === "1"){
        $(document).ready(function(){
            $('#natureModal').modal('show')
            $('#gotIt').click(function(){
                window.location.replace("http://127.0.0.1:5000/nature");
            });
        });
    } 
    else if (event.target.value === '2'){
        window.location.replace('http://127.0.0.1:5000/party')
    }
    else if (event.target.value === '3'){
        window.location.replace('http://127.0.0.1:5000/food')
    }
    else if (event.target.value === '4'){
        window.location.replace('http://127.0.0.1:5000/culture')
    }
}