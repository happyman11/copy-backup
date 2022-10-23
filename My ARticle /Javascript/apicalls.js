
function testapi()
{
var config = {
                method: 'get',
                url: 'https://v2.jokeapi.dev/joke/Any?safe-mode',
                headers: { 
                            'Authorization': 'Bearer glpat-KBEF6VQzFXrmcDtxGzq5', 
                            'Content-Type': 'text/plain'
                         },
                data : {}
            
            };

let testinfo=document.getElementById("test")

axios(config)
.then(function (response) 
                            {
                                console.log(JSON.stringify(response.data));
                                let data=response.data; 

                            }
        )
.catch(function (error) 
                        {
                            console.log(error);
                        }
        )

                    }



// MAss mail APi saved template

function tmassmailcallsavedtemplate()
{
var config = {
                method: 'get',
                url: 'https://v2.jokeapi.dev/joke/Any?safe-mode',
                headers: { 
                            'Authorization': 'Bearer glpat-KBEF6VQzFXrmcDtxGzq5', 
                            'Content-Type': 'text/plain'
                         },
                data : {}
            
            };

let testinfo=document.getElementById("test")

axios(config)
.then(function (response) 
                            {
                                console.log(JSON.stringify(response.data));
                                let data=response.data; 

                            }
        )
.catch(function (error) 
                        {
                            console.log(error);
                        }
        )

                    }

//Mass mail call api via template by api

function testapi()
{
var config = {
                method: 'get',
                url: 'https://v2.jokeapi.dev/joke/Any?safe-mode',
                headers: { 
                            'Authorization': 'Bearer glpat-KBEF6VQzFXrmcDtxGzq5', 
                            'Content-Type': 'text/plain'
                         },
                data : {}
            
            };

let testinfo=document.getElementById("test")

axios(config)
.then(function (response) 
                            {
                                console.log(JSON.stringify(response.data));
                                let data=response.data; 

                            }
        )
.catch(function (error) 
                        {
                            console.log(error);
                        }
        )

                    }

