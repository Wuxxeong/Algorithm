// Run by Node.js
const readline = require('readline');
let total = 0;
let count = 0;
let N = 0;
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		if (count == 0){
			N = Number(line);
			count++;
			continue;
		}
		let [c, v] = line.split(' ');
		
		if(c=='in') 
			total += Number(v);
		else if(c=='out')
			total -= Number(v);
		
		count++;
		if(total < 0){
			console.log("fail");
			break;
			rl.close();
		}
	}
	if (total >= 0) {
		console.log("success");
	}
	process.exit();
})();
