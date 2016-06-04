
CC := gcc
CXX := g++
AR := ar
CFLAGS := -Wall

INCLUDE := 

THIRD_PARTY := ./3rdparty
GTEST_LIB_NAME := gtest
GTEST_STATIC_LIB := lib$(GTEST_LIB_NAME).a
GTEST_DIR := $(THIRD_PARTY)/gtest
GTEST_INC_DIR := $(GTEST_DIR)/include
GTEST_SRC_DIR := $(GTEST_DIR)/src
INCLUDE += -I$(GTEST_INC_DIR) -I$(GTEST_DIR)

FOO_NAME := foo
BAR_NAME := bar

INC_DIR := ./include
SRC_DIR := ./src
FOO_SRC_DIR := $(SRC_DIR)/$(FOO_NAME)
BAR_SRC_DIR := $(SRC_DIR)/$(BAR_NAME)

LIB_DIR := ./lib
OBJ_DIR := ./obj
FOO_OBJ_DIR := $(OBJ_DIR)/$(FOO_NAME)
BAR_OBJ_DIR := $(OBJ_DIR)/$(BAR_NAME)
BIN_DIR := ./bin

BUILD_DIRS := $(LIB_DIR) \
	$(OBJ_DIR) $(FOO_OBJ_DIR) $(BAR_OBJ_DIR)\
	$(BIN_DIR)

# OBJECTS for our foobar project
OBJ := $(FOO_NAME)/foo.o
OBJS := $(addprefix $(OBJ_DIR)/, $(OBJ))

INCLUDE += -I$(INC_DIR)

CFLAGS += $(INCLUDE)

DEPS := $(wildcard $(INC_DIR)/*.h)

all: dirs 3rdparty test

test: $(OBJS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cc $(DEPS)
	@echo "CXX\t $@"
	@$(CXX) $(CFLAGS) -c $< -o $@

3rdparty: gtest 
	
gtest: $(LIB_DIR)/$(GTEST_STATIC_LIB)

$(LIB_DIR)/$(GTEST_STATIC_LIB): $(OBJ_DIR)/gtest-all.o
	@echo "AR\t $@"
	@$(AR) -r $@ gtest-all.o

$(OBJ_DIR)/gtest-all.o: $(GTEST_SRC_DIR)/gtest-all.cc
	@echo "CXX\t $@"
	@$(CXX) $(CFLAGS) -isystem -pthread -c $(GTEST_SRC_DIR)/gtest-all.cc

.PHONY: dirs clean 3rdparty

dirs:
	@mkdir -p $(BUILD_DIRS)

clean:
	@rm -rf $(BUILD_DIRS)
