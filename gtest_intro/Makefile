
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
INCLUDE += -I$(GTEST_INC_DIR)

LIB_DIR := ./lib
INC_DIR := ./include
SRC_DIR := ./src
OBJ_DIR := ./obj
BIN_DIR := ./bin

INCLUDE += $(INC_DIR)

CFLAGS += $(INCLUDE)

$(LIB_DIR)/$(GTEST_STATIC_LIB):
	$(CXX) $(CFLAGS)
