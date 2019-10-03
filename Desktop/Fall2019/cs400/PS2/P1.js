
const fib = function*(n, n1 = 0, n2 = 1){

    if (n === 0) { return n1; }
    yield n1;  yield *fib(n-1, n2, n1 + n2);
}

const fibs = n => fib(20)
myFibs = fibs()

const isEven= function* (){
    let count = 0;
    while (count < 6) {
        temp = myFibs.next().value
        if(temp % 2 == 0){  yield temp;  }
    }
}

const even = n => isEven()
myEven = even()

let c = 6;
while (c --> 0) { console.log(myEven.next().value) }
