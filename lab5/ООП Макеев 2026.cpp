#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Base {
  public :
   Base() { cout << "! CONSTRUCTOR: Base() Default\n\n"; }
   Base(Base *obj) { cout << "! CONSTRUCTOR: Base(Base *obj) Argumentic\n\n"; }
   Base(int x) { cout << "! CONSTRUCTOR: Base(int x) Argumentic\n\n"; a_ = x; }
   Base(Base &obj) { cout << "! CONSTRUCTOR: Base(Base &obj) Copy\n\n"; }
   virtual ~Base() { cout << "! DESTRUCTOR: ~Base()\n\n"; }

   void Print() {
      cout << "base void print()\n";
   }

   virtual void PrintOwnAtrs() {
     cout << "Base private: " << a_ << '\n';
   }

   virtual void PrintOwnAtrsReversed() {
     cout << 100 - a_%100 << '\n';
   }

   

   void Method1() {
     Print();
   }

   void Method2() {
    PrintOwnAtrs();
   }

   void NonVirt() {
    cout << "Base NonVirt() \n";
   }
   
   virtual void Virt() {
     cout << "Base Virt() \n";
   }

   virtual string classname() {
    return "Base";
   }

   virtual bool isA(string classname) {
     return classname == "Base";
   }
   private:
     int a_ = 0;
};

class Desc : public Base {
  public:
   Desc() { cout << "! CONSTRUCTOR: Desc() Default\n\n"; }
   Desc(Desc *obj) { cout << "! CONSTRUCTOR: Desc(Desc *obj) Argumentic\n\n"; }
   Desc(int x) {
     cout << "! CONSTRUCTOR: Desc(int x) Argumentic\n\n";
     b_ = x;
     arr_ = new int(x);
   }
   Desc(Desc &obj) { cout << "! CONSTRUCTOR: Desc(Desc &obj) Copy\n\n"; }
   ~Desc() {
     cout << "! DESTRUCTOR: ~Desc()\n\n";
     delete arr_;
   }

   void Print() {
     cout << "desc void print()\n";
   }

   void PrintOwnAtrs() override {
     cout << "Desc private: " << b_ << '\n';
   }

   void PrintOwnAtrsReversed() {
     cout << 100 - b_ % 100 << '\n';
   }

   void NonVirt() {
     cout << "Desc NonVirt() \n";
   }
   void Virt() {
     cout << "Desc Virt() \n";
   }

   string classname() override {
     return "Desc";
   }
   bool isA(string classname) override {
     return classname == "Desc";
   }
   private:
     int b_ = 0;
     int* arr_;
};

void f1(Base  obj) {
  cout << "\nf1\n";
  cout << obj.classname() << endl;
  Desc* x = dynamic_cast<Desc*>(&obj);
  if (x) {
    cout << x->classname() << endl;
  } else {
    cout << "x was nullptr\n";
  }
  
}

void f2(Base  *obj) {
  cout << "\nf2\n";
  cout << obj->classname() << endl;
  Desc *x = dynamic_cast<Desc *>(obj);
  if (x) {
    cout << x->classname() << endl;
  }
  else {
    cout << "x was nullptr\n";
  }
}

void f3(Base  &obj) {
  cout << "\nf3\n";
  cout << obj.classname() << endl;
  Desc *x = dynamic_cast<Desc *>(&obj);
  if (x) {
    cout << x->classname() << endl;
  }
  else {
    cout << "x was nullptr\n";
  }
}

Base func1() {
  Base A;
  return A;
};

Base* func2() {
  Base B;
  return &B;
};

Base& func3() {
  Base C;
  return C;
};

Base func4() {
  Base* A = new Base();
  return *A;
};

Base* func5() {
  Base* B = new Base();
  return B;
};

Base& func6() {
  Base* C = new Base();
  return *C;
};

void ReceiveUnique(unique_ptr<Base> b) {
  cout << "void ReceiveUnique(unique_ptr<Base> b)\n";
  cout << b->classname() << endl;
  // ReturnUnique(b);
}

unique_ptr<Base> ReturnUnique(unique_ptr<Base> b) {
  cout << "unique_ptr<Base> ReturnUnique(unique_ptr<Base> b)\n";
  return b;
}

void ReceiveShared(shared_ptr<Desc> b) {
  cout << "void ReceiveShared(shared_ptr<Base> b)\n";
  cout << b->classname() << endl;
}

shared_ptr<Desc> CreateShared() {
  shared_ptr<Desc> x = make_shared<Desc>(148);
  x->PrintOwnAtrs();
  // x = ReturnShared(x);
  return x;
}

shared_ptr<Desc> ReturnShared(shared_ptr<Desc> d) {
  cout << "shared_ptr<Base> ReturnShared(shared_ptr<Desc> d)\n";
  return d;
}

int main() {
  Base* b0 = new Desc(5);
  delete b0;

  cout << "b1\n";
  Base* b1 = new Desc;
  cout << "d1\n";
  Desc* d1 = new Desc;

  // shadow
  cout << "\n ** shadow \n";
  b1->Print();
  d1->Print();

  // virtual
  cout << "\n ** virtual \n";
  b1->PrintOwnAtrs();
  d1->PrintOwnAtrs();
  
  // virt destr
  cout << "\n ** virt destr\n";
  delete b1;
  delete d1;

  // methods
  cout << "\n ** methods\n";
  Base* b2 = new Base();
  Base* bd2 = new Desc;
  Desc* d2 = new Desc;
  d2->Method1(); // использовали просто папкин принт?

  d2->Method2(); // использовали просто свооой принт?

  bd2->NonVirt(); // Base
  d2->NonVirt(); // Desc

  bd2->Virt(); // Base -> Desc
  d2->Virt(); // Base -> Desc

  // classname & isA
  cout << "\n ** classname & isA \n";
  cout << "b2 name: " << b2->classname() << endl;
  cout << "bd2 name: " << bd2->classname() << endl;
  cout << "d2 name: " << d2->classname() << endl;

  cout << "b2 is b2: " << b2->isA(b2->classname()) << endl;
  cout << "bd2 is bd2: " << bd2->isA(bd2->classname()) << endl;
  cout << "d2 is d2: " << d2->isA(d2->classname()) << endl;


  cout << "b2 is d2: " << b2->isA(d2->classname()) << endl;
  cout << "b2 is bd2: " << b2->isA(bd2->classname()) << endl;

  cout << "d2 is b2: " << d2->isA(b2->classname()) << endl;
  cout << "d2 is bd2: " << d2->isA(bd2->classname()) << endl;

  cout << "bd2 is d2: " << bd2->isA(d2->classname()) << endl;
  cout << "bd2 is b2: " << bd2->isA(b2->classname()) << endl;

  cout << "\n ** unsafe & isA \n";
  if (bd2->isA("Desc")) {
    Desc* unsafe = (Desc*)bd2;
    unsafe->Print();
  }
  cout << "dynamic\n";
  Base* safe1 = dynamic_cast<Base*>(bd2);
  Desc* safe2 = dynamic_cast<Desc*>(bd2);
  safe1->Print();
  safe2->Print();


  delete b2, bd2, d2;

  // three funcs
  cout << "\n ** three funcs \n";
  Desc d3;
  Desc* d4 = new Desc();

  Base b3;
  Base* b4 = new Base();
  f1(d3);
  f1(*d4);
  f1(b3);
  f1(*b4);

  f2(&d3);
  f2(d4);
  f2(&b3);
  f2(b4);

  f3(d3);
  f3(b3);
  f3(*d4);
  f3(*b4);


  // six funcs
  cout << "\n six funcs \n";

  cout << "\nfunction1 \n";
  
  // auto x1 = func1();
  
  cout << func1().classname() << endl;

  cout << "\nfunction2 \n";
  auto x2 = func2();

  cout << "\nfunction3 \n";
  auto x3 = func3();

  cout << "\nfunction4 \n";
  // auto x4 = func4();
  cout << func4().classname() << endl;

  cout << "\nfunction5 \n";
  auto x5 = func5();

  cout << "\nfunction6 \n";
  auto x6 = func6();

  // unique & shared 
  cout << "\n***uniqie***\n";
  unique_ptr<Base> uq1 = make_unique<Base>(5);
  uq1->PrintOwnAtrs();
  // unique_ptr<Base> uq2 = ReturnUnique(uq1);

  {
    // unique_ptr<Base> uq3 = uq1;
    unique_ptr<Base> uq3 = make_unique<Base>(500);
    uq3->PrintOwnAtrs();
  }

  unique_ptr<Base> uq4 = move(uq1);
  uq4->PrintOwnAtrs();

  cout << "uq1.reset()\n";
  uq1.reset();

  cout << "\n***sharie***\n";
  shared_ptr<Desc> sh1 = make_shared<Desc>(100);
  cout << "sh1 shares: " << sh1.use_count() << endl;

  {
    shared_ptr<Desc> sh2 = sh1;
    cout << "sh1 shares: " << sh1.use_count() << endl;
    sh2->PrintOwnAtrs();
  }

  cout << "sh1 shares: " << sh1.use_count() << endl;
  shared_ptr<Desc> sh3 = ReturnShared(sh1);
  shared_ptr<Desc> sh4 = CreateShared();
  cout << "sh3 shares: " << sh3.use_count() << endl;
  cout << "sh3 was owner before: " << sh3.owner_before(sh1) << endl;
  cout << "sh4 shares: " << sh4.use_count() << endl;
  sh3.reset();
  sh1.reset();
}
