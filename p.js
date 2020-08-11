
function Node(op, left, right) {
    this.op = op;
    this.left = left;
    this.right = right;
}

Node.prototype.evaluate = function () {
    let left = this.left;
    let right = this.right;

    if (left.evaluate !== undefined)//(typeof left !== "number")
        left = left.evaluate();
    if (right.evaluate !== undefined)//(typeof right !== "number")
        right = right.evaluate();


    if (this.op === "+")
        return left + right;

    if (this.op === "-")
        return left - right;

    if (this.op === "*")
        return left * right;

    if (this.op === "/")
        return left / right;

    if (this.op === "^")
        return left ** right;
};

//------------------------------

parseToTree = function (expr) {
    if (!expr.includes("+") && !expr.includes("-") && !expr.includes("*") && !expr.includes("/") && !expr.includes("^"))
        return parseFloat(expr);

    var idxAdd = searchPlus(expr);
    var idxSub = searchMinus(expr);
    var idxMul = searchDivMul(expr, '*');
    var idxDiv = searchDivMul(expr, '/');
    var idxPow = searchPow(expr);

    if (idxAdd !== -1) {
        left = expr.substr(0, idxAdd)
        if (idxAdd === 0)
            left = "0"
        right = expr.substr(idxAdd + 1)
        console.log(left)
        console.log(right)
        return new Node("+", parseToTree(left), parseToTree(right))
    } else if (idxSub !== -1) {
        left = expr.substr(0, idxSub)
        if (idxSub === 0)
            left = "0"
        right = expr.substr(idxSub + 1)
        return new Node("-", parseToTree(left), parseToTree(right))
    } else if (idxMul !== -1) {
        left = expr.substr(0, idxMul)
        right = expr.substr(idxMul + 1)

        return new Node("*", parseToTree(left), parseToTree(right))
    } else if (idxDiv !== -1) {
        left = expr.substr(0, idxDiv)
        right = expr.substr(idxDiv + 1)
        return new Node("/", parseToTree(left), parseToTree(right))
    } else if (idxPow !== -1) {
        left = expr.substr(0, idxPow)
        right = expr.substr(idxPow + 1)
        return new Node("^", parseToTree(left), parseToTree(right))
    } else if (expr[0] === "(") {
        left = 0
        right = expr.substr(1, searchClosingPar(expr) - 1)
        return new Node('+', left, parseToTree(right))
    }
}

searchMinus = function (expr) {
    parenthesisCounter = 0
    for (var i = expr.length - 1; i > -1; i--) {
        if (expr[i] === ")")
            parenthesisCounter += 1;
        else if (expr[i] === "(")
            parenthesisCounter -= 1;
        else if (expr[i] === '-' && parenthesisCounter === 0) {
            if (expr[i - 1] === "+" ||
                expr[i - 1] === "-" ||
                expr[i - 1] === "*" ||
                expr[i - 1] === "/" ||
                expr[i - 1] === "^")
                continue
            return i
        }
    }
    if (searchPlus(expr) === -1) {
        if (expr[0] === "-")
            return 0
    }
    return -1
}

searchPow = function (expr) {
    parenthesisCounter = 0
    for (let i = 0; i < expr.length; i++) {
        var char = expr[i];
        if (char === "(")
            parenthesisCounter += 1
        else if (char === ")")
            parenthesisCounter -= 1
        else if (char === "^" && parenthesisCounter === 0)
            return i
    }
    return -1
}

searchClosingPar = function (expr) {
    parenthesisCounter = 0
    for (let i = 0; i < expr.length; i++) {
        c = expr[i]
        if (i === 0 && c === '(')
            continue
        if (c === "(")
            parenthesisCounter += 1
        else if (c === ")")
            parenthesisCounter -= 1
        else if (c === ")" && parenthesisCounter === 0)
            return i
    }
    return -1
}

searchPlus = function (expr) {
    parenthesisCounter = 0;
    for (var i = 0; i < expr.length; i++) {
        if (expr[i] === "(") {
            parenthesisCounter += 1;
        } else if (expr[i] === ")") {
            parenthesisCounter -= 1;
        } else if (expr[i] === "+" && parenthesisCounter === 0) {
            if (expr[i - 1] === "+" ||
                expr[i - 1] === "-" ||
                expr[i - 1] === "*" ||
                expr[i - 1] === "/" ||
                expr[i - 1] === "^")
                continue;
            return i;
        }
    }
    return -1;
}

searchDivMul = function (expr, c) {
    parenthesisCounter = 0
    for (var i = expr.length - 1; i > -1; i--) {
        if (expr[i] === ")")
            parenthesisCounter += 1
        else if (expr[i] === "(")
            parenthesisCounter -= 1
        else if (expr[i] === c && parenthesisCounter === 0)
            return i
    }
    return -1
}

var expr = "5+2+3+5*2";
console.log(parseToTree(expr).evaluate());
console.log("actual answer:" + eval(expr))