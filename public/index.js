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
        let contextualErrors = receivedData.contextual
        

        let successful = true

        let resultLog = ""
        console.log(receivedData);

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
       if (contextualErrors.length){

            contextualErrors.forEach(e => {
                console.log(e);

                if (!e.found){
                    resultLog = resultLog + `CONTEXTUAL ERROR: name '${e.ident}' is not defined\n`
                }else{
                    if (e.requiredParams > e.givenParams){
                        resultLog = resultLog + `CONTEXTUAL ERROR: ${e.ident}() missing ${e.requiredParams - e.givenParams} required positional `
                        
                        if (e.requiredParams - e.givenParams > 1){
                            resultLog = resultLog + `arguments: `
                            

                            let args = e.args
                            for (let i = e.givenParams; i < args.length; i++) {
                                if (i == args.length -1){
                                    resultLog += ' and '
                                }
                                resultLog = resultLog + `'${args[i]}'`
                                if (i+1 < args.length -1){
                                    resultLog += ', '
                                }
                            }
                        
                        
                        }else{
                            resultLog = resultLog + `argument: '${e.args[e.givenParams]}'`
                        }

                        

                    }else{
                        resultLog = resultLog + `CONTEXTUAL ERROR: ${e.ident}() takes ${e.requiredParams} positional arguments but ${e.givenParams} ${(e.givenParams == 1) ? "was" : "were"} given\n`

                    }
                }
                   
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

