var http = require("http");
var Pandorabot = require('pb-node');

var options = {
  url: 'https://aiaas.pandorabots.com',
  app_id: '1409616272199',
  user_key: 'e8a6d54095d026bff5031b37a0df2f53',
  botname: 'rosiebot'
};

var bot = new Pandorabot(options);
var port = 4000;
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
			var talkParams = {input: body};
			bot.talk(talkParams, function (err, res) {
				if (!err) {
					console.log(res);
					response.end(res.responses[0]);
				}
			});
        });
	}
    else
    {
        console.log("POST not received");
        var html = '<html><body>Only http POST allowed with header: text/plain</body></html>';
        response.writeHead(200, {'Content-Type': 'text/html'});
        response.end(html);
    }
});