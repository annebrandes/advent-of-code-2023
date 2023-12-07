#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <sstream>

int main() {
    std::ifstream file("day2-input.txt");
    std::string line;

    if (!file) {
        std::cerr << "Unable to open file";
        return 1;
    }

    int game_sum = 0;

    while (getline(file, line)) {

        std::istringstream iss(line);
        std::string temp;
        int game_num;
        iss >> temp >> game_num;    

        std::regex redRegex("(\\d+) red");
        std::regex greenRegex("(\\d+) green");
        std::regex blueRegex("(\\d+) blue");

        std::smatch match;

        int red = 0, green = 0, blue = 0;
        std::string tempLine = line;

        while (std::regex_search(tempLine, match, redRegex)) {
            red = std::max(red, std::stoi(match[1].str()));
            tempLine = match.suffix();
        }
        
        tempLine = line;

        while (std::regex_search(tempLine, match, greenRegex)) {
            green = std::max(green, std::stoi(match[1].str()));
            tempLine = match.suffix();
        }
        
        tempLine = line;

        while (std::regex_search(tempLine, match, blueRegex)) {
            blue = std::max(blue, std::stoi(match[1].str()));
            tempLine = match.suffix();
        }

        std::cout << "Red: " << red << ", Green: " << green << ", Blue: " << blue << std::endl;

        int powers = red * blue * green;
        game_sum += powers;
    }

    std::cout << "Game sum: " << game_sum << std::endl;
    return game_sum;
}
