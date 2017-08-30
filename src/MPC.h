#ifndef MPC_H
#define MPC_H

#include <vector>
#include "Eigen-3.3/Eigen/Core"

using namespace std;

class MPC {
 public:
  MPC(double latency);

  virtual ~MPC();

  // Solve the model given an initial state and polynomial coefficients.
  // Return the first actuatotions.
  vector<double> Solve(Eigen::VectorXd state, Eigen::VectorXd coeffs);

  void getPredictedWaypoints(vector<double> &x_predicted, vector<double> &y_predicted);

  std::vector<double> x_predicted, y_predicted;

  double previous_delta, previous_a;

  int n_latency;
};

#endif /* MPC_H */
