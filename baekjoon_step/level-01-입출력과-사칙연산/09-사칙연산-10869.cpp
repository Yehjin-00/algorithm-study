// Title: 사칙연산
// Level: 1_09
// Number: 10869
// Date: 2021.02.12

#include <iostream>

int main(){
    int a, b;
    std::cin >> a >> b;

    std::cout << a+b << std::endl;
    std::cout << a-b << std::endl;
    std::cout << a*b << std::endl;
    std::cout << a/b << std::endl;
    std::cout << a%b << std::endl;
}

// std::endl 이게 \n 이라고 보면 됨.
// std::cout과 cin 시에 << 혹은 >> 로 쭉 이어서 써도 됨.
// std::cin >> 사이는 white space 인 것 같음.
// https://coding-factory.tistory.com/479