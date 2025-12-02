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
        Dial(int size, int start_idx);
        void move_dial(char dir, int num);
    private:
        DialClick* create_dial(int size, int start_idx);
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

Dial::Dial(int size, int start_idx) {
    pos = create_dial(size, start_idx);
    count = 0;
}

void Dial::move_dial(char dir, int num) {
    for (int i = 0; i < num; i++) {
        if (dir == 'R') pos = pos->next;
        else pos = pos->prev;
        if (pos->val == 0) count += 1;
    }
}

DialClick* Dial::create_dial(int size, int start_idx) {
    DialClick *res = nullptr;
    DialClick *start = nullptr;
    DialClick* prev = nullptr;
    for (int i = 0; i < size; i++) {
        // prev->print();
        std::cout << "Creating " << i << std::endl;
        
        DialClick *newClick = new DialClick(i, prev);
        // newClick->print();
        
        if (prev) prev->next = newClick;
        // prev->print();
        
        prev = newClick;
        if (i == 0) {
            start = newClick;
        } else if (i == size - 1) {
            prev->next = start;
            start->prev = prev;
        } else if (i == start_idx) {
            res = newClick;
        }
    }
    
    start->print();
    res->print();
    return res;
}

int main() {
    std::ifstream f("input.txt");

    if (!f.is_open()) {
        std::cerr << "Error opening the file!";
        return 1;
    }

    std::string s;
    int count = 0;
    
    Dial* dial = new Dial(100, 50);
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
