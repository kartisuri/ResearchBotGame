var mitsuku = require('mitsuku-api')();

function mitsuku(body){
	var response = "";
	if (body.search(/\bgame\b|\bexperiment\b|\bresearch\b/i) !== -1){
		response = "Sorry! I don't know";
		console.log("Bot: Sorry! I don't know");
	} else if (body.search(/\bhi\b/i) !== -1) {
		response = "Hi there";
		console.log("Bot: Hi there");
	} else {
		mitsuku.send(body).then(function(result) {
			if (result.search(/mitsuku/i) !== -1){
				result = "Sorry! I don't know";
			}
			console.log("Bot: " + result);
			response = result;
		});
	}
	return response;
}