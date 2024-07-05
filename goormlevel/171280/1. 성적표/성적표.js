// // Run by Node.js
// const readline = require('readline');
// let dict = {};
// let result = 0;
// let max = -1;
// let count = 0;
// let N=0, M=0;
// (async () => {
// 	let rl = readline.createInterface({ input: process.stdin });
	
// 	for await (const line of rl) {
// 		if(count == 0){
// 			[N,M] = line.split(' ').map(Number);
// 			count++;
// 			continue;
// 		}
// 		let [c,v] = line.split(' ').map(Number);
// 		if(!Object.keys(dict).map(Number).includes(c)){
// 			dict[c] = [v];
// 		}
// 		else{
// 			dict[c].push(v);
// 		}
// 	}
// 	// console.log(dict);
// 	for(k of Object.keys(dict)){
// 		let sum = 0, avg = 0;
// 		for(v of dict[k]){
// 			sum += v;
// 		}
// 		avg = sum/(dict[k].length);
// 		// console.log(k, avg);
// 		if(avg > max){
// 			max = avg;
// 			result = Number(k);
// 		}
// 		if(avg == max){
// 			result = result>Number(k)?result:Number(k);
// 		}
// 	}
// 	console.log(result);
// 	rl.close();
// 	process.exit();
// })();

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M] = input[0].split(' ').map(Number);
  let scores = new Map();

  for (let i = 1; i <= N; i++) {
    const [C, S] = input[i].split(' ').map(Number);
    if (!scores.has(C)) {
      scores.set(C, []);
    }
    scores.get(C).push(S);
  }

  let maxAverage = -1;
  let bestSubject = M + 1;

  for (let [subject, marks] of scores) {
    const total = marks.reduce((a, b) => a + b, 0);
    const average = total / marks.length;

    if (average > maxAverage || (average === maxAverage && subject < bestSubject)) {
      maxAverage = average;
      bestSubject = subject;
    }
  }

  console.log(bestSubject);
});

