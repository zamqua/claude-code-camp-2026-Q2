#include <iostream>
#include <memory>
#include <string>

class Buffer {
public:
  Buffer(int size) {
    data = std::make_unique<char[]>(size);
    std::cout << "Buffer allocated\n";
  }

private:
  std::unique_ptr<char[]> data;
};

int main() {
  Buffer b1(100);
  Buffer b2 = std::move(b1);
  return 0;
}
