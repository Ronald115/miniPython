const express = require("express");
const fs = require('fs');
const app = express()
const path = require("path")
const bodyParser = require("body-parser")
const {PythonShell} = require('python-shell');

//Settings
app.set('port',3000)
app.set('public', path.join(__dirname, 'public'))


const codeFolder = path.join(__dirname, 'code')

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


page=path.join(app.get('public'),'/index.html')

app.get("/", (req,res) =>{
    res.sendFile(page)
})

app.post('/compiler', (req,res) => {
    var filepath = path.join(codeFolder, 'text.txt')
    var fileContent = req.body.code
    fs.writeFile(filepath, fileContent, (err) => {
        if (err) throw err;
   
        let options = {
            args: [filepath],
            pythonPath: path.join(__dirname,'venv/Scripts/python.exe')
        }
        
        PythonShell.run('main.py', options, (err, results) => {
            if (err) throw err;
            // results is an array consisting of messages collected during execution
            data = JSON.parse(results[0])
            res.send(data)
        });
    
    }); 

})


app.use(express.static('public'));

app.listen(app.get('port'), () =>{
    console.log(`Server on port ${app.get('port')}`);

})

