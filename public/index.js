var compile = document.querySelector(".boton")
var fileButton = document.querySelector("#fileButton")



compile.addEventListener('click', async ()=>{
    var code = document.querySelector(".codeTA")

    dataToSend = {"code" : code.value}
    const response = await fetch("http://localhost:3000/compiler", {
    method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(dataToSend),
    });
    response.json().then(receivedData => {
        let result = document.querySelector("#result")

        let parserErrors = receivedData.parser
        let lexerErrors = receivedData.lexer
        
        let successful = true

        let resultLog = ""

        if (lexerErrors.length){

            lexerErrors.forEach(e => {
                resultLog = resultLog + `LEXER ERROR: when scanning line ${e.line} column ${e.column}: ${e.msg}\n`
            });

            successful = false
        }

        if (parserErrors.length){

            parserErrors.forEach(e => {
                resultLog = resultLog + `PARSER ERROR: when parsing line ${e.line} column ${e.column}: ${e.msg}\n`
            });

            successful = false
        }

        result.classList.remove("redText")
        result.classList.remove("greenText")
        

        if (successful){
            result.classList.add("greenText")
            result.innerHTML = "Compilation Successful"
        }else{
            result.classList.add("redText")
            result.innerHTML = resultLog
        }

    });
      

})

fileButton.addEventListener('click', () => {

    let input = document.createElement('input');
    input.type = 'file';
    input.onchange = () => {
      // you can use this method to get file and perform respective operations
        let files =   Array.from(input.files);
        let file = files[0]
        if (file) {
      
            var reader = new FileReader();
            reader.readAsText(file, "UTF-8");
            reader.onload =  (evt) => {
                let codeTA = document.querySelector(".codeTA")
                console.log(codeTA.innerHTML);
                code.innerHTML = evt.target.result;
                console.log(evt.target.result);
            }
            reader.onerror = _ => {
                console.log("error reading file");
            }

         
        }
    };
    input.click();
})

