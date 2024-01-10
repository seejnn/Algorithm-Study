function solution(my_string, k) {
    var answer = '';
    console.log(Array.from(Array(k).keys()))
    return Array.from(Array(k).keys()).map((el) => my_string).join('');
}