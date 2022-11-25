function count(x) {
    c = 0;

    for (i = 0; i < x; i++){
        c += i;
    }

    return c;
}

bool = true
var x;

switch(count(3)){
    case 2 : 
        break;
    case 10 : 
        x = 'sepuluh';
        break;
    default:
        x = "default";
}

var i = 0;
while (x == 'sepuluh'){
    if (i == 0){
        continue;
    }
    else{
        bool = false;
    }
    i++
}