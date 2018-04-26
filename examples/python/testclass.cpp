#include "testclass.h"

/** Dummy constructor.
 */
TestClass::TestClass(int _dim0, int _dim1)
{
  dim0 = _dim0;
  dim1 = _dim1;
}

/** Initialize matrices.
 */
void TestClass::init0(void)
{
  a = arma::mat(dim0, dim1);
  b = arma::mat(dim1, dim0);

  for (uint i = 0; i < dim0; i++)
  {
    for (uint j = 0; j < dim1; j++)
    {
      a(i, j) = ((double)i * 1.0 + (double)j * 0.1) * 0.1;
      b(j, i) = ((double)i * 1.0 + (double)j * 0.1) * 0.1;
    }
  }
}

/** Initialize matrices.
 */
void TestClass::init1(void)
{
  arma::mat im = arma::linspace<arma::ucolvec>(0, dim0 - 1, dim0) * arma::ones<arma::colvec>(dim1).t();
  arma::mat jm = arma::ones<arma::colvec>(dim0) * arma::linspace<arma::ucolvec>(0, dim1 - 1, dim1).t();
  a = (im + jm * 0.1) * 0.1;  
  b = a.t();
}

/** Calculate norm(a * b).
 */
double TestClass::func0(void)
{
  return arma::norm(a * b, "fro");
}

