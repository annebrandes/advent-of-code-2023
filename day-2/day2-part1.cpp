#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("day2-input.txt");
    std::string line;

    if (!file) {
        std::cerr << "Unable to open file";
        return 1;
    }

    while (getline(file, line)) {
        std::cout << line << std::endl;
    }

    return 0;
}
