var http = require('http');
var fs = require('fs');
var app = http.createServer(function(request,response){
    var url = request.url;
    if(request.url == '/'){
      url = '/index.html';
    }
    else if(request.url == '/Desktop___2.html'){
      url = '/Desktop___2.html';
    }
    else if(request.url == '/Desktop___3.html'){
      url = '/Desktop___3.html';
    }
    if(request.url == '/favicon.ico'){
      response.writeHead(404);
      response.end();
      return;
    }
    response.writeHead(200);
    response.end(fs.readFileSync(__dirname + url));
});
app.listen(3000);
