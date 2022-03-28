var compile = document.querySelector(".boton")
var code = document.querySelector(".codeTA")
var result = document.querySelector("#result")





compile.addEventListener('click', async ()=>{

    result.innerHTML = "Pellejo"
    code.innerHTML = "Pe"
    






    data = {"code" : 'print(x)'}
    const response = await fetch("http://localhost:3000/compiler", {
    method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
    });
    response.json().then(data => {
        console.log(data);
    });
      
   
})