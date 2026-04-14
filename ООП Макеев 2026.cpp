#include <iostream>
#include <string>
using namespace std;

class Payment {
 public:
   Payment() {
     cout << "! Payment default constructor Payment()! \n";
  }

   Payment(int x) {
     value_ = x;
     cout << "! Payment argument constructor Payment(int x)! \n";
   }

   Payment(const Payment& p) {
     value_ = p.value_;
     cout << "! Payment copy constructor Payment(const Payment& p)! \n";
   }

   ~Payment() {
     cout << "! Payment destructor ~Payment()! \n";
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
    cout << "! Coin default constructor Coin()! \n";
  }

  Coin(int x, string s) :Payment(x), material_(s) {
    cout << "! Coin argument constructor Coin(int x, string s)! \n";
  }

  Coin(int x) : Payment(x), material_(to_string(x) + "-like") {
    cout << "! Coin argument constructor Coin(int x)! \n";
  }


  Coin(const Coin &c) : Payment(c), material_(c.material_) {
    cout << "! Coin copy constructor Coin(const Coin &c)! \n";
  }

  ~Coin() {
    cout << "! Coin destructor ~Coin()! \n";
    cout << "! Before deletion of Coin material was: " + material_ + '\n'+ '\n';
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
    cout << "! Card default constructor Card()! \n";
  }

  Card(string s) {
    passport_id_ = s;
    cout << "! Card argument constructor Card(string s)! \n";
  }

  Card(int x, string s) : Payment(x), passport_id_(s) {
    cout << "! Card argument constructor Card(int x, string s)! \n";
  }

  Card(int x) : Payment(x), passport_id_(to_string(x) + "-like") {
    cout << "! Card argument constructor Card(int x)! \n";
  }

  Card(const Card& k) : Payment(k), passport_id_(k.passport_id_) {
    cout << "! Card copy constructor Card(const Card& k)! \n";
  }

  ~Card() {
    cout << "! Card destructor ~Card()! \n";
    cout << "! Before deletion of Card passport was: " + passport_id_ + '\n'+ '\n';
  }
  string ReturnInfo() {
    auto x = Payment::ReturnInfo();
    return x + " " + passport_id_;
  }

   string ReturnPassport() {
     return passport_id_;
  }

   void ChangePassport(string s) {
     cout << "! Lets change Card passport! \n";
     passport_id_ = s;
   }
 private:
  string passport_id_ = "0000";
};

class Wallet {
 public:
  Coin my_coin;
  Card* my_card;

   Wallet() : my_coin() {
     cout << "!! Wallet default constructor Wallet(), Coin and now Card too!\n\n";
     my_card = new Card();
  }
   Wallet(int x) : my_coin(x/2) {
     my_card = new Card(x - x/2);
     cout << "!! Wallet argument constructor Wallet(int x), give a halve to coin&card\n\n";
   }

   Wallet(const Wallet &w) : my_coin(w.my_coin) {
     my_card = new Card(*(w.my_card));
     cout << "!! Wallet copy constructor Wallet(const Wallet &w), lets copypaste\n\n";
   }

   ~Wallet() {
     cout << "!!   Wallet destructor ~Wallet(), sequence start\n";
     cout << "!! delete my_card, bye-bye card! \n";
     delete my_card;
     cout << "!! Wallet destructor, Bye-bye wallet\n\n";
  }
};

int main() {
  // composition of objects
  Wallet x1 = Wallet();
  Wallet x2 = x1;
  Wallet* x3 = new Wallet(x2);
  x1.my_coin.ChangeMaterial("fayans");
  x1.my_card->ChangePassport("xoxo");

  x2.my_card->ChangePassport("x2x2");
  x2.my_coin.ChangeMaterial("sugar");

  x3->my_card->ChangePassport("x3x3");
  x3->my_coin.ChangeMaterial("cinnamon");

  // buncha constructors
  Coin c1 = Coin();
  Payment* p1 = new Payment();
  Payment p2(10);
  Payment* p3 = new Payment(p2);
  Coin* c2 = new Coin(20, "gold");
  Coin* c3 = new Coin(*c2);
  cout << endl;

  // buncha basic outputs
  cout << "p1 info: " << p1->ReturnInfo() << endl;
  cout << "p1 value: " << p1->ReturnValue() << endl << endl;

  cout << "p2 info: " << p2.ReturnInfo() << endl;
  cout << "p2 value: " << p2.ReturnValue() << endl << endl;

  cout << "p3 info: " << p3->ReturnInfo() << endl;
  cout << "p3 value: " << p3->ReturnValue() << endl << endl;

  cout << "c1 info: " << c1.ReturnInfo() << endl;
  cout << "c2 info: " << c2->ReturnInfo() << endl;
  cout << "c3 info: " << c3->ReturnInfo() << endl << endl;

  // check ChangeMaterial()
  c3->ChangeMaterial("silver");
  cout << "c2 info: " << c2->ReturnInfo() << endl;
  cout << "c3 info: " << c3->ReturnInfo() << endl << endl;

  // check copy using "="
  Coin c4 = c1;
  cout << "c1 info: " << c1.ReturnInfo() << endl;
  cout << "c4 info: " << c4.ReturnInfo() << endl << endl;

  // check if copy c4 of c1 would change c1
  c4.ChangeMaterial("lead");
  cout << "c1 info: " << c1.ReturnInfo() << endl;
  cout << "c4 info: " << c4.ReturnInfo() << endl << endl;

  // check parent* = new child();
  Payment* k1 = new Card();
  cout << "k1 has: " + k1->ReturnInfo() + '\n';
  delete k1;

  // k2 uses both own & parent's methods
  Card* k2 = new Card("8530");
  cout << "k2 has: " + k2->ReturnPassport() + '\n';
  cout << "k2 also has: " + k2->ReturnInfo() + '\n';
  cout << "k2 also also has: " + to_string(k2->ReturnValue()) + '\n' + '\n';


  // check copy using "="
  Card* k3 = k2;
  cout << "k3 has: " + k3->ReturnPassport() + '\n';

  // check if copy k3 of k2 would change k2
  k3->ChangePassport("7777");
  cout << "k2 after k3 changed: " + k2->ReturnPassport() + '\n';
  cout << "k3 after k3 changed: " + k3->ReturnPassport() + '\n' + '\n';

  // check parent = child()
  Payment k4 = Card(-1, "????");
  cout << "k4 has: " + k4.ReturnInfo() + '\n';

  delete k3;
  // delete k2;
  delete p1;
  delete p3;
  delete c3;
  delete c2;
  delete x3;
}
