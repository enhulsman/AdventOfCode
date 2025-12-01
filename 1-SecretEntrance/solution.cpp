#include <fstream>
#include <iostream>
#include <string>

class DialClick {
    public:
        int val;
        DialClick* next;
        DialClick* prev;
        DialClick(int i, DialClick* p);
        void print();
};

class Dial {
    public:
        int count;
        DialClick* pos;
        Dial(DialClick* start);
        void move_dial(char dir, int num);
};

DialClick::DialClick(int i, DialClick* p) {
    val = i;
    prev = p;
    next = nullptr;
}

void DialClick::print() {
    int p = -1, n = -1;
    if (prev) p = prev->val;
    if (next) n = next->val;
    std::cout << p << " - " << val << " - " << n << std::endl;
}

Dial::Dial(DialClick* start) {
    pos = start;
    count = 0;
}

void Dial::move_dial(char dir, int num) {
    for (int i = 0; i < num; i++) {
        if (dir == 'R') pos = pos->next;
        else pos = pos->prev;
        if (pos->val == 0) count += 1;
    }
}

DialClick* create_dial(int max) {
    DialClick *zero = new DialClick(0, nullptr);
    DialClick* prev = zero;
    
    for (int i = 1; i < max; i++) {
        // prev->print();
        // std::cout << "Creating " << i << std::endl;
        
        DialClick *newClick = new DialClick(i, prev);
        // newClick->print();
        
        prev->next = newClick;
        // prev->print();
        
        prev = prev->next;
        if (i == max - 1) {
            prev->next = zero;
            zero->prev = prev;
        }
    }
    
    return zero;
}

int main() {
    std::ifstream f("input.txt");

    if (!f.is_open()) {
        std::cerr << "Error opening the file!";
        return 1;
    }

    std::string s;
    int count = 0;
    
    Dial* dial = new Dial(create_dial(100));
    dial->move_dial('R', 50);


    while (getline(f, s)) {
        int num = stoi(s.substr(1));
        dial->move_dial(s[0], num);

        // std::cout << s[0] << num << std::endl;
    }

    std::cout << dial->count << std::endl;

    f.close();
    return 0;
}
