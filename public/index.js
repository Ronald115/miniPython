var compile = document.querySelector(".boton")






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

        
        result.innerHTML = resultLog
    });
      

})