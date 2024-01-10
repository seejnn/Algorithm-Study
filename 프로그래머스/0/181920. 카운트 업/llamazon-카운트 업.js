function solution(start, end) {
    var answer = [];
    let temp = start;

    for(let i = 0; i <= end - start; i++){
        answer.push(temp);
        temp++;
    }
    return answer;
}
