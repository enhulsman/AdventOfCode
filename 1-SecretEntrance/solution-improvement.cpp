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
        void move_dial(char dir, int num, int part);
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

void Dial::move_dial(char dir, int num, int part) {
    for (int i = 0; i < num; i++) {
        if (dir == 'R') pos = pos->next;
        else pos = pos->prev;
        if (pos->val == 0 && part == 2) count += 1;
    }
    if (pos->val == 0 && part == 1) count += 1;
}

DialClick* Dial::create_dial(int size, int start_idx) {
    DialClick*   res = nullptr;
    DialClick*  prev = nullptr;
    DialClick* start = nullptr;

    for (int i = 0; i < size; i++) {
        DialClick *newClick = new DialClick(i, prev);
        
        if (prev) prev->next = newClick;
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
    
    return res;
}

int solve(int part) {
    std::ifstream f("input.txt");

    if (!f.is_open()) {
        std::cerr << "Error opening the file!";
        return 1;
    }

    std::string s;
    int count = 0;
    
    Dial* dial = new Dial(100, 50);

    while (getline(f, s)) {
        int num = stoi(s.substr(1));
        dial->move_dial(s[0], num, part);
    }

    f.close();
    return dial->count;
}

int main(int argc, char *argv[]) {
    using namespace std;
    if (argc < 2) {
        cout << "1: " << solve(1) << endl;
        cout << "2: " << solve(2) << endl;
    } else if (argc == 2) {
        int part = atoi(argv[1]);
        if (part == 1 || part == 2) {
            cout << solve(part) << endl;
        } else {
            cerr << "Invalid part to solve. Enter 1 or 2 (or none for both)" << endl;
        }
    }

    return 0;
}
