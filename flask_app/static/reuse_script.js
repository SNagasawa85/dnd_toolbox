function rollstat(){
    let statRoll = document.getElementById('statRoll');
    let statVal = document.getElementById('statVal');
    let top3 = [];
    let d6roller = '';
    let rolls = {};
    let d6Drop1 = 0;
    for(var i = 1 ; i < 5 ; i++){
        rolls[i]=Math.floor(Math.random() * 6) +1;
    }
    console.log(rolls);
    for(key in rolls){
        d6roller += "Roll# " + key + " is " + rolls[key] + "!  ";
        top3.push(rolls[key]);
        }
    top3.sort();
    top3.reverse();
    top3.pop();
    for( var i = 0; i <top3.length ; i++){
        d6Drop1 += top3[i]
    }
    statVal.innerText = d6Drop1.toString();
    console.log(d6roller)
    console.log(d6Drop1);
    statRoll.innerText = d6roller.toString();
}
