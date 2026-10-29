#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Row {
protected:
    string inf;
public:
    //дефолтний конструктор
    Row(): inf("") {
        cout<<"Default row constructor"<<endl;
    }
    //конструктор з параметром
    Row(const string& INF): inf(INF) {
        cout<<"Row parameter constructor"<<endl;
    }
    //копіювальний конструктор
    Row(const Row& other): inf(other.inf) {
        cout<<"Row copy constructor"<<endl;
    }
    //деструктор
    ~Row() {
        cout<<"Row destructor: \""<<inf<<"\"\n";
    }
    //знайти підрядок у рядку
    bool findRow(const string& same) const {
    size_t pos=inf.find(same);
    if (pos==string::npos)
        return false;
    else
        return true;
    }
    //вставити символ у даному рядку
    void insertSymbol(size_t pos, char symbol) {
        if (pos>inf.size()) pos=inf.size();
        inf.insert(inf.begin() + pos, symbol);
    }
    //очищення заданого рядка
    void clearRow() {
        inf.clear();
    }
    //вивід рядка
    void printRow() const {
        cout<<"\""<<inf<< "\"\n";
    }
};

class Text : public Row {
private:
    vector<Row> rows;

public:
    //деф конструктор
    Text() : Row() {
        cout<<"Text default constructor"<<endl;
    }
    //конструктор з параметром
    Text(const vector<Row>& v) : Row(), rows(v) {
        cout<<"Text parameter constructor"<<endl;
    }
    //копіювальний конструктор
    Text(const Text& other) : Row(other), rows(other.rows) {
        cout<<"Text copy constructor"<<endl;
    }
    //деструктор
    ~Text() {
        cout<<"Text destructor"<<endl;
    }

    Row getLine(int index) const {
        return rows[index];
    }

    //-----------додатковий метод: вставити символ у конкретний рядок тексту--------------------
    void insertSymbolInLine(size_t lineIndex, size_t pos, char symbol) {
        if (lineIndex >= rows.size()) return;
        rows[lineIndex].insertSymbol(pos, symbol);
    }

    //-----------додатковий метод: знайти підрядок у якомусь рядку------------------------
    bool findRowInText(const string& same) const {
    for (int i=0; i<(int)rows.size(); i++) {
        if (rows[i].findRow(same)) {
            return true;
        }
    }
    return false;
}

    //вивести текст
    void printText() const {
        for (int i=0; i<(int)rows.size(); i++) {
            cout<<i<<": ";
            rows[i].printRow();
        }
    }
};

int main() {
//========================================Рядок==================================
    string s;
    cout<<"Enter one row: ";
    getline(cin, s);

    Row r1(s);
    r1.printRow();

    cout<<"Enter substring to find: ";
    string sub;
    getline(cin, sub);

    cout<<"Find \""<<sub<<"\" in row: "<<(r1.findRow(sub) ? "found\n" : "not found\n");

    cout<<"Enter position and symbol to insert: ";
    size_t pos;
    char symbol;
    cin>>pos>>symbol;
    cin.ignore();

    r1.insertSymbol(pos, symbol);
    r1.printRow();

    r1.clearRow();
    cout<<"Row after cleared"<<endl;
    r1.printRow();

//=============================================Текст============================
    vector<Row> v;
    string line;

    cout<<"Enter 3 rows for text:"<<endl;
    for (int i=0; i<3; i++) {
        cout<<"Row "<<i<<": ";
        getline(cin, line);
        v.push_back(Row(line));
    }

    Text t(v);
    cout<<"\nText:\n";
    t.printText();

    cout<<"\nEnter line index, position and symbol to insert: ";
    size_t lineIndex;
    cin>>lineIndex>>pos>>symbol;
    cin.ignore();

    t.insertSymbolInLine(lineIndex, pos, symbol);
    cout<<"\nText after inserting symbol:\n";
    t.printText();

    cout<<"\nEnter substring to find in text: ";
    getline(cin, sub);

    cout<<"Find \""<<sub<<"\" in text: "<<(t.findRowInText(sub) ? "found\n" : "not found\n");

    return 0;
}
