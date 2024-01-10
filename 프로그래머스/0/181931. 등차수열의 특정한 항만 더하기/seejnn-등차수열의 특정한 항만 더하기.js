function solution(a, d, included) {
    var answer = 0;
    
    for(i = 0; i < included.length; i++) {
        if(included[i] == true) {
            answer += a + d * i
        }
    }
    
    return answer;
}