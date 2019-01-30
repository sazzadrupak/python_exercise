var foo = function () {
    var i = 0;
    return function () {
        console.log(i);
        i++;
    };
}();

foo();
foo();