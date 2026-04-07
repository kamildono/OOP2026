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
     cout << "! Before deletion of Payment value was : " + to_string(value_) + '\n' + '\n';
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

  Coin(const Coin &c) : Payment(c), material_(c.material_) {
    cout << "! Coin copy constructor! \n";
  }

  ~Coin() {
    cout << "! Coin destructor! \n";
    cout << "! Before deletion of Coin material was: " + material_ + '\n';
  }

  void ChangeMaterial(string s) {
    cout << "! Lets change Coin material! \n";
    material_ = s;
  }

  string ReturnInfo() {
    int output_int = ReturnValue();
    return material_ + "en " + to_string(output_int);
  }
 private:
  string material_ = "n/a";
};

class Card : public Payment {
 public:
  Card() {
    cout << "! Card default constructor! \n";
  }

  Card(string s) {
    passport_id_ = s;
    cout << "! Card argument constructor! \n";
  }

  Card(const Card& k) : Payment(k), passport_id_(k.passport_id_) {
    cout << "! Card copy constructor! \n";
  }

  ~Card() {
    cout << "! Card destructor! \n";
    cout << "! Before deletion of Card passport was: " + passport_id_ + '\n';
  }
  string ReturnInfo() {
    auto x = Payment::ReturnInfo();
    return x + " " + passport_id_;
  }

   string GetPassport() {
     return passport_id_;
  }

   void ChangePassport(string s) {
     cout << "! Lets change Card passport! \n";
     passport_id_ = s;
   }
 private:
  string passport_id_ = "0000";
};



int main() {
  Coin c1 = Coin();
  Payment* p1 = new Payment();
  Payment p2(10);
  Payment* p3 = new Payment(p2);
  Coin* c2 = new Coin(20, "gold");
  Coin* c3 = new Coin(*c2);

  cout << endl;

  cout << "p1 info: " << p1->ReturnInfo() << endl;
  cout << "p1 value: " << p1->ReturnValue() << endl;

  cout << endl;

  cout << "p2 info: " << p2.ReturnInfo() << endl;
  cout << "p2 value: " << p2.ReturnValue() << endl;

  cout << endl;

  cout << "p3 info: " << p3->ReturnInfo() << endl;
  cout << "p3 value: " << p3->ReturnValue() << endl;

  cout << endl;

  cout << "c1 info: " << c1.ReturnInfo() << endl;

  cout << "c2 info: " << c2->ReturnInfo() << endl;
  cout << "c3 info: " << c3->ReturnInfo() << endl;

  cout << endl;

  c3->ChangeMaterial("silver");
  cout << "c2 info: " << c2->ReturnInfo() << endl;
  cout << "c3 info: " << c3->ReturnInfo() << endl;

  cout << endl;

  Coin c4 = c1;

  cout << "c1 info: " << c1.ReturnInfo() << endl;
  cout << "c4 info: " << c4.ReturnInfo() << endl;

  cout << endl;

  c4.ChangeMaterial("lead");
  cout << "c1 info: " << c1.ReturnInfo() << endl;
  cout << "c4 info: " << c4.ReturnInfo() << endl;

  cout << endl;

  Payment* k1 = new Card();
  cout << "k1 has: " + k1->ReturnInfo() + '\n';
  delete k1;

  Card* k2 = new Card("8530");
  cout << "k2 has: " + k2->GetPassport() + '\n';
  cout << "k2 also has: " + k2->ReturnInfo() + '\n';
  cout << "k2 also also has: " + to_string(k2->ReturnValue()) + '\n';

  cout << endl;

  Card* k3 = k2;
  cout << "k3 has: " + k3->GetPassport() + '\n';
  k3->ChangePassport("7777");

  cout << "k2 after k3 changed: " + k2->GetPassport() + '\n';
  cout << "k3 after k3 changed: " + k3->GetPassport() + '\n';

  cout << endl;

  delete k3;
  // delete k2;
  delete p1;
  delete p3;
  delete c3;
  delete c2;
}
