function solution(number, n, m) {
    var answer = 0;
    number % n === 0 && number % m == 0 ? answer = 1 : answer = 0
    return answer;
}