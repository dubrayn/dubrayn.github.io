CXX = g++
CXXFLAGS = -Wall -O3 -std=c++14
LDFLAGS =
LIBS = -larmadillo
TARGET = main
OBJS = main.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(LDFLAGS) $^ -o $@ $(LIBS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) $< -c -o $@

.PHONY: clean
clean:
	rm -f $(OBJS)
	rm -f $(TARGET)
