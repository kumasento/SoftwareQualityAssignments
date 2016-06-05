#ifndef BAR_H__
#define BAR_H__

template <typename T>
class EquationSolver {
/**
 * This class will gracefully solve a equation as:
 * a * x^2 + b * x + c = 0 (1)
 */
public:
  /**
   * solve: Given all parameters, will create a equation and solve it
   * @ param a: a in the equation (1), could be 0
   * @ param b: b in the equation (1), could be 0
   * @ param c: c in the equation (1), could be 0
   * @ param x: Pointer to equation solutions.
   * @ return: Number of solutions, can only be 0, 1, 2.
   */
  static int solve(T a, T b, T c, T *x);
};

#endif
