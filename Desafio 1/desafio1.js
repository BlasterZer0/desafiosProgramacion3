let array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
let a = 0;
let b = 0;
let c = 0;

function format(a) {
    if (a <= 9) {
        a = "00"+a;
    }
    if (a >= 10 & a <= 99) {
        a = "0"+a;
    }
    return a;
}

const length = array.length;

for (let i = 0; i <= 999; i++) {
    const counter = format(i);
    console.log(array[c] + array[b] + array[a] + counter);
    if (i == 999) {
        a++;
        i = 0;
        if (a == length) {
            a = 0;
            b++
        }
        if (b == length) {
            b = 0;
            c++
        }
        if (c == length) {
            break
        }
    }
}