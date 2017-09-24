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
			var headers = {};
			headers["Access-Control-Allow-Origin"] = "*";
			headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS";
			headers["Access-Control-Allow-Credentials"] = false;
			headers["Access-Control-Max-Age"] = '86400'; // 24 hours
			headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept";
			response.writeHead(200, headers);
			if (body.search(/\bgame\b|\bexperiment\b|\bresearch\b/i) !== -1){
				console.log("I am not telling you!");
				response.end("I am not telling you!");
			} else if (body.search(/\bhi\b/i) !== -1) {
				console.log("Hi there");
				response.end("Hi there");
			} else if (body.search(/\bwhat is up\b|\bwhats up\b/i) !== -1) {
				console.log("Nothing");
				response.end("Nothing");
			} else {
				mitsuku.send(body).then(function(result) {
					if (result.search(/mitsuku|creator/i) !== -1){
						result = "I am not telling you!"
					}
					console.log(result);
					response.end(result);
				});
			}
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