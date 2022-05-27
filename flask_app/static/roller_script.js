let die = 0;
let curDie = document.getElementById('selected');
let dieNum = 1;
let curNum = document.getElementById('amount');
let type = '';
let curType = document.getElementById('type');
let rolls = document.getElementById('rolls');
let result = document.getElementById('results');

// dice rolling function (boutta get long AF)

function rollDice(){
    let rollVals = '';
    let values = {};
    let numbers = [];
    
    for(var i = 1 ; i <= dieNum; i++ ){
        values[i]=Math.floor(Math.random() * die) +1;
        numbers.push(values[i]);
    }
    console.log(numbers)
    for(key in values){
        rollVals += 
        `
        <span>Roll #${key} is ${values[key]}</span><br>
        
        ` 
    }
    rolls.innerHTML = rollVals;
    let temp = numbers[0];
    if( type === 'Advantage'){
        for(var i = 1; i < numbers.length ; i++){
            if(numbers[i] > temp){
                temp = numbers[i];
            } 
        }   
        console.log(numbers)
        result.innerText = "You roll: " + temp;
        return 
    }
    else if( type === 'Normal'){
        console.log('norm')
        result.innerText = 'You roll: ' + numbers;
        return
    }
    else if( type === 'Disadvantage'){
        for(var i = 1; i < numbers.length ; i++){
            if(numbers[i] < temp){
                temp = numbers[i];
            } 
        }   
        console.log(numbers)
        result.innerText = 'You roll: ' + temp;
        return
    }

}

function selectDie(val){
    curDie.innerText = 'You have selected D' + val;
}

function selectNum(num){
    dieNum = num;
    curNum.innerText = 'You have Chosen ' + dieNum + ' dice to roll.'
    
}

function selectRoll(rollType){
    type = rollType;
    curType.innerText = 'You have selected ' + type + ' roll';
}
let dieOption = [4,6,8,10,12,20]

function makeDieBig(id){
    for(var i = 0; i<dieOption.length; i ++){
        if(dieOption[i] !== id){
            document.getElementById(dieOption[i]).style.height='90px';
            document.getElementById(dieOption[i]).style.width='90px';
        }
        document.getElementById(id).style.height='121px';
        document.getElementById(id).style.width='121px';
    }
}



function resetDice(){
    for(i = 0; i <dieOption.length; i++){
        document.getElementById(dieOption[i]).style.height='90px';
        document.getElementById(dieOption[i]).style.width='90px';
    }
}