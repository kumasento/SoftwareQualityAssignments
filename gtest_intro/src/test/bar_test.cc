
#include "gtest/gtest.h"
#include "bar.h"

EquationSolver<float> *equation_solver = NULL;

TEST(FloatEquationSolverTest, ZeroSolutionTest) {
  EXPECT_EQ(0, equation_solver->solve());
}

int main(int argc, char *argv[]) {
  ::testing::InitGoogleTest(&argc, argv);

  equation_solver = new EquationSolver<float>();
  return RUN_ALL_TESTS();
}
