#include <iostream>
#include <string>
using namespace std;

class Payment {
 public:
   Payment() {
     cout << "! Payment constructor! \n";
  }

   Payment(int x) {
     value_ = x;
     cout << "! Payment argument constructor! \n";
   }

   Payment(const Payment& p) {
     value_ = p.value_;
     cout << "! Payment copy constructor! \n";
   }

   ~Payment() {
     cout << "! Payment destructor! \n";
   }

   string ReturnInfo() {
     return to_string(value_);
   }

   int ReturnValue() {
     return value_;
   }
  private:
   int value_ = 0;
};

class Coin : Payment {
 public:
  Coin() {
    cout << "! Coin constructor! \n";
  }

  Coin(int x, string s) :Payment(x), material_(s) {
    cout << "! Coin argument constructor! \n";
  }

  ~Coin() {
    cout << "! Coin destructor! \n";
  }

  string ReturnInfo() {
    int output_int = ReturnValue();
    return material_ + "en " + to_string(output_int);
  }
 private:
  string material_ = "n/a";
};

class Card : Payment {

};

int main() {
  Coin* c1 = new Coin();
  Payment* p1 = new Payment();
  Payment p2(10);
  Payment* p3 = new Payment(p2);
  Coin* c2 = new Coin(20, "gold");

  cout << "p1 info: " << p1->ReturnInfo() << endl;
  cout << "p1 value: " << p1->ReturnValue() << endl;

  cout << "p2 info: " << p2.ReturnInfo() << endl;
  cout << "p2 value: " << p2.ReturnValue() << endl;

  cout << "p3 info: " << p3->ReturnInfo() << endl;
  cout << "p3 value: " << p3->ReturnValue() << endl;

  cout << "c1 info: " << c1->ReturnInfo() << endl;

  cout << "c2 info: " << c2->ReturnInfo() << endl;

  delete c1;
  delete p1;
  delete p3;
  delete c2;
}
