function solution(x, n) {
    var answer = [];
    var temp = 0;
    
    for(i = 0; i < n; i++) {
        temp += x
        answer.push(temp)
    }
    
    return answer;
}