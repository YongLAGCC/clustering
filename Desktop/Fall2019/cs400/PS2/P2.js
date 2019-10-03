const splitSents = function* ( sentence ){

    var words = str.split(" ");
    for (var k = 0; k < words.length ; k++) {
        yield words[k]
    }
}

const str = "All I know is something like a bird within her sang";
var words = str.split(" ")

const split = n => splitSents(str)
mySplit= split()

let c = words.length;
while (c --> 0) {

    console.log(mySplit.next().value);
}


