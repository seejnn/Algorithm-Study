function solution(n) {
    var answer = 0;
    
    for(i = 1; i < 10000000; i++) {
        if(n % i == 1) {
            return i
        }
    }
    
    return answer;
}