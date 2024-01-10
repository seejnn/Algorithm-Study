function solution(start, end_num) {
    var answer = [];
    
    for(i = start; i >= end_num; i--) {
        answer.push(i)
    }
    
    return answer;
}