var http = require("http");
var mitsuku = require('mitsuku-api')();

var port = 5000;

var server = http.createServer().listen(port, '0.0.0.0');
console.log("Server is listening at " + port);
server.on('request', function(request, response) {
	if (request.method == 'POST')
	{
		var body = '';
		console.log("POST");
        request.on('data', function (data) {
            body += data;
        });
        request.on('end', function () {
            console.log("User: " + body);
			response.writeHead(200, {'Content-Type': 'text/plain'});
			mitsuku.send(body).then(function(result)
			{
				console.log("Bot: " + result);
				response.end(result);
			});
        });
	}
    else
    {
        console.log("GET");
        var html = '<html><body>Only http POST allowed with header: text/plain</body></html>';
        response.writeHead(200, {'Content-Type': 'text/html'});
        response.end(html);
    }
});