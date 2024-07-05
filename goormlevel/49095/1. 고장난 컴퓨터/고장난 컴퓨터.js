// Run by Node.js
const readline = require('readline');
let isFirst = true;
let N=0, c=0;
let seconds = [];
let word_count=1;
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		if(isFirst){
			[N,c] = line.split(' ');
			isFirst=false;
			continue;
		}
		seconds = line.split(' ').map(Number);
		for(let i=1; i<N; i++){
			word_count++;
			if(seconds[i]-seconds[i-1] > c){
				word_count = 1;
			}
		}
	}
	console.log(word_count);

	rl.close();
	process.exit();
})();
