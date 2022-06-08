var compile = document.querySelector(".boton")
var fileButton = document.querySelector("#fileButton")

var codeEditor = document.getElementById('code');
var lineCounter = document.getElementById('lineCounter');

codeEditor.addEventListener('scroll', () => {
    lineCounter.scrollTop = codeEditor.scrollTop;
    lineCounter.scrollLeft = codeEditor.scrollLeft;
});

codeEditor.addEventListener('keydown', (e) => {
    if (e.key === 'Tab'){
        e.preventDefault();
        var start = codeEditor.selectionStart;
        var end = codeEditor.selectionEnd;
    
        // set textarea value to: text before caret + tab + text after caret
        codeEditor.value = codeEditor.value.substring(0, start) +
          "    " + codeEditor.value.substring(end);
    
        // put caret at right position again
        codeEditor.selectionStart = codeEditor.selectionEnd = start + 1;
    }
})




var lineCountCache = 0;
function line_counter() {
      var lineCount = codeEditor.value.split('\n').length;
      var outarr = new Array();
      if (lineCountCache != lineCount) {
         for (var x = 0; x < lineCount; x++) {
            outarr[x] = (x + 1) + '.';
         }
         lineCounter.value = outarr.join('\n');
      }
      lineCountCache = lineCount;
}
codeEditor.addEventListener('input', () => {
    line_counter();
});

compile.addEventListener('click', async ()=>{
    var code = document.querySelector("#code")
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

        let errors = receivedData.errors
        let output = receivedData.output

        let parserErrors = errors.parser
        let lexerErrors = errors.lexer
        let contextualErrors = errors.contextual
        let typeErrors = errors.typeErrors
        let runtimeErrors = errors.runtimeErrors
        console.log(runtimeErrors);
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
       if (contextualErrors.length){

            contextualErrors.forEach(e => {
                console.log(e);

                if (!e.found){
                    resultLog = resultLog + `Name Error: name '${e.ident}' is not defined\n`
                }else{
                    if (e.requiredParams > e.givenParams){
                        resultLog = resultLog + `Type Error: ${e.ident}() missing ${e.requiredParams - e.givenParams} required positional `
                        
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
                            resultLog += '\n'
                        
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
        
        if (typeErrors.length){

            typeErrors.forEach(e => {
                resultLog = resultLog + `TypeError: '${e.type}' is not `
                if (e.call){
                    resultLog += `callable\n`
                }else{
                    resultLog += `suscriptable\n`
                }
               
            });

            successful = false
        }
    
        if (runtimeErrors.length){
            runtimeErrors.forEach(e => {
                resultLog = resultLog + e +'\n';
            });
            successful = false
        }

        result.classList.remove("redText")
        result.classList.remove("whiteText")
        
        if (successful){
            result.innerHTML = output + "\n\nCompilation successful"
            
            result.classList.add("whiteText")
           
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
                codeEditor.value = evt.target.result;
                console.log(evt.target.result);
            }
            reader.onerror = _ => {
                console.log("error reading file");
            }

         
        }
    };
    input.click();
})
