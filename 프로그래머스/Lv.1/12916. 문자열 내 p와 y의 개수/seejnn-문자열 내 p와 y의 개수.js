function solution(s){
    var answer = true;
    var count_p = 0;
    var count_y = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    
    
    for(i = 0; i < s.length; i++) {
        if(s[i] === "p") {
            count_p += 1
        } else if(s[i] === "P") {
            count_p += 1
        }
    }
    
    for(i = 0; i < s.length; i++) {
        if(s[i] === 'y') {
            count_y += 1
        } else if (s[i] === 'Y') {
            count_y += 1
        }
    }
    

    if(count_p + count_y == 0) {
            return answer = true
        } else {
            if(count_p == count_y) {
            return answer = true
        } else return answer = false
        }
        

    return answer;
}