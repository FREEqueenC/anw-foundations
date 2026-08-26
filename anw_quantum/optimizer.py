"""
ANW Foundations - Quantum-Inspired Optimization Engine
Module: anw_quantum.optimizer
Author: ANW Foundations (Ashleigh Walker)

Provides:
- QUBO (Quadratic Unconstrained Binary Optimization) & Ising Matrix Models
- Simulated Quantum Annealing (SQA) via Path-Integral Transverse Field Emulation
- Levity Protocol Liquidity Pool Band Optimizer (LEV/USDC)
- Multi-Agent Autonomous Task DAG Scheduler
"""

import math
import random
from typing import List, Dict, Tuple, Optional, Callable


class QUBOProblem:
    """Represents a Quadratic Unconstrained Binary Optimization (QUBO) problem:
    Minimize E(x) = x^T Q x + c^T x = sum_{i<=j} Q_ij * x_i * x_j
    where x_i in {0, 1}.
    """
    def __init__(self, size: int, name: str = "QUBO_Instance"):
        self.size = size
        self.name = name
        # Q matrix stored as dictionary of (i, j) -> weight with i <= j
        self.matrix: Dict[Tuple[int, int], float] = {}

    def set_linear(self, i: int, weight: float):
        """Set linear coefficient Q_ii."""
        if 0 <= i < self.size:
            self.matrix[(i, i)] = self.matrix.get((i, i), 0.0) + weight

    def set_quadratic(self, i: int, j: int, weight: float):
        """Set quadratic interaction coefficient Q_ij."""
        if 0 <= i < self.size and 0 <= j < self.size:
            u, v = min(i, j), max(i, j)
            self.matrix[(u, v)] = self.matrix.get((u, v), 0.0) + weight

    def evaluate(self, state: List[int]) -> float:
        """Calculate energy for binary state vector x in {0, 1}^N."""
        energy = 0.0
        for (i, j), weight in self.matrix.items():
            if state[i] * state[j] == 1:
                energy += weight
        return energy

    def to_ising(self) -> Tuple[Dict[int, float], Dict[Tuple[int, int], float], float]:
        """Convert QUBO (x in {0,1}) to Ising Hamiltonian (s in {-1, 1})
        x_i = (s_i + 1) / 2
        Returns (h_linear, J_coupling, offset).
        """
        h: Dict[int, float] = {i: 0.0 for i in range(self.size)}
        J: Dict[Tuple[int, int], float] = {}
        offset = 0.0

        for (i, j), Q_ij in self.matrix.items():
            if i == j:
                h[i] += Q_ij / 2.0
                offset += Q_ij / 2.0
            else:
                J[(i, j)] = Q_ij / 4.0
                h[i] += Q_ij / 4.0
                h[j] += Q_ij / 4.0
                offset += Q_ij / 4.0
        return h, J, offset


class QuantumInspiredAnnealer:
    """Simulated Quantum Annealing (SQA) engine.
    Uses Trotterized multi-replica transverse-field Hamiltonian simulation
    to achieve quantum tunneling through high and narrow potential energy barriers.
    """
    def __init__(
        self,
        qubo: QUBOProblem,
        num_trotter_replicas: int = 8,
        num_sweeps: int = 600,
        gamma_initial: float = 3.0,
        gamma_final: float = 0.01,
        temperature: float = 0.5
    ):
        self.qubo = qubo
        self.P = num_trotter_replicas
        self.num_sweeps = num_sweeps
        self.gamma_init = gamma_initial
        self.gamma_final = gamma_final
        self.temp = max(1e-4, temperature)

    def solve(self, seed: Optional[int] = None) -> Dict[str, any]:
        if seed is not None:
            random.seed(seed)

        N = self.qubo.size
        P = self.P
        # Initialize P replicas with random binary states {0, 1}
        replicas = [[random.choice([0, 1]) for _ in range(N)] for _ in range(P)]

        best_state = replicas[0][:]
        best_energy = self.qubo.evaluate(best_state)
        energy_history: List[float] = [best_energy]

        for sweep in range(self.num_sweeps):
            progress = sweep / max(1, self.num_sweeps - 1)
            # Anneal transverse field Gamma (Quantum fluctuation control)
            gamma = self.gamma_init * ((self.gamma_final / self.gamma_init) ** progress)
            # Quantum coupling between Trotter slices
            j_perp = -0.5 * self.temp * math.log(max(1e-8, math.tanh(max(1e-6, gamma / (P * self.temp)))))

            for p in range(P):
                p_prev = (p - 1) % P
                p_next = (p + 1) % P

                for i in range(N):
                    current_val = replicas[p][i]
                    flipped_val = 1 - current_val

                    # Classical energy delta within slice p
                    delta_classical = 0.0
                    for j in range(N):
                        if i == j:
                            delta_classical += self.qubo.matrix.get((i, i), 0.0) * (flipped_val - current_val)
                        else:
                            u, v = min(i, j), max(i, j)
                            weight = self.qubo.matrix.get((u, v), 0.0)
                            if weight != 0.0:
                                delta_classical += weight * (flipped_val - current_val) * replicas[p][j]

                    delta_classical /= P

                    # Quantum Trotter coupling delta across adjacent time slices
                    # Spin mapping: s = 2*x - 1
                    s_curr = 2 * current_val - 1
                    s_flip = 2 * flipped_val - 1
                    s_prev = 2 * replicas[p_prev][i] - 1
                    s_next = 2 * replicas[p_next][i] - 1

                    delta_quantum = -j_perp * (s_flip - s_curr) * (s_prev + s_next)
                    total_delta = delta_classical + delta_quantum

                    # Metropolis-Hastings transition acceptance
                    if total_delta <= 0.0 or random.random() < math.exp(-total_delta / self.temp):
                        replicas[p][i] = flipped_val

            # Track best energy across all Trotter replicas
            for p in range(P):
                e = self.qubo.evaluate(replicas[p])
                if e < best_energy:
                    best_energy = e
                    best_state = replicas[p][:]

            if sweep % max(1, self.num_sweeps // 50) == 0:
                energy_history.append(best_energy)

        return {
            "optimal_state": best_state,
            "optimal_energy": best_energy,
            "history": energy_history,
            "qubo_name": self.qubo.name,
            "trotter_slices": self.P,
            "sweeps": self.num_sweeps
        }


class LevityLiquidityOptimizer:
    """Optimizes Uniswap v3 / Base Mainnet LP distribution for LEV/USDC pool.
    Finds binary band allocation x_b in {0,1} to maximize fee yields while penalizing
    volatility slippage and impermanent loss risk.
    """
    def __init__(self, price_bins: List[float], expected_volumes: List[float], volatility: float = 0.45):
        self.bins = price_bins
        self.volumes = expected_volumes
        self.volatility = volatility
        self.num_bins = len(price_bins)

    def build_qubo(self, max_active_bins: int = 4, target_capital: float = 10000.0) -> QUBOProblem:
        qubo = QUBOProblem(size=self.num_bins, name="Levity_LP_Optimization")

        # Yield reward (negative energy) and volatility risk
        for i, (price, vol) in enumerate(zip(self.bins, self.volumes)):
            expected_fee_yield = 0.003 * vol  # 0.3% pool tier
            il_risk = self.volatility * (abs(price - 1.0) ** 2) * 100.0
            linear_cost = -expected_fee_yield + il_risk
            qubo.set_linear(i, linear_cost)

        # Correlation penalties for adjacent overlapping bands
        for i in range(self.num_bins):
            for j in range(i + 1, self.num_bins):
                dist = abs(i - j)
                if dist == 1:
                    qubo.set_quadratic(i, j, 15.0)  # encourage diversified spacing

        # Constraint penalty: (sum(x_i) - max_active_bins)^2
        penalty_lambda = 45.0
        for i in range(self.num_bins):
            # linear expansion: lambda * (1 - 2*k) * x_i
            qubo.set_linear(i, penalty_lambda * (1 - 2 * max_active_bins))
            for j in range(i + 1, self.num_bins):
                qubo.set_quadratic(i, j, 2 * penalty_lambda)

        return qubo


class AgentTaskScheduler:
    """Schedules autonomous AI agent tasks across parallel worker nodes
    minimizing makespan, communication latency, and execution cost.
    """
    def __init__(self, tasks: List[Dict[str, any]], num_workers: int = 3):
        self.tasks = tasks
        self.num_tasks = len(tasks)
        self.num_workers = num_workers
        self.total_variables = self.num_tasks * self.num_workers

    def _var_idx(self, task_i: int, worker_w: int) -> int:
        return task_i * self.num_workers + worker_w

    def build_qubo(self) -> QUBOProblem:
        qubo = QUBOProblem(size=self.total_variables, name="NICOLE_Agent_Task_Scheduler")

        # 1. Base execution cost of task on worker
        for i, task in enumerate(self.tasks):
            base_duration = task.get("duration", 10.0)
            for w in range(self.num_workers):
                worker_efficiency = 1.0 + 0.2 * w
                idx = self._var_idx(i, w)
                qubo.set_linear(idx, base_duration * worker_efficiency)

        # 2. Constraint: Each task MUST be assigned to exactly ONE worker
        # Penalty: lambda * (sum_w x_{i,w} - 1)^2
        lambda_assignment = 80.0
        for i in range(self.num_tasks):
            for w in range(self.num_workers):
                idx = self._var_idx(i, w)
                qubo.set_linear(idx, lambda_assignment * (1 - 2 * 1))
            for w1 in range(self.num_workers):
                for w2 in range(w1 + 1, self.num_workers):
                    idx1 = self._var_idx(i, w1)
                    idx2 = self._var_idx(i, w2)
                    qubo.set_quadratic(idx1, idx2, 2 * lambda_assignment)

        # 3. Workload balancing: minimize difference in assigned durations
        lambda_balance = 5.0
        for w in range(self.num_workers):
            for i in range(self.num_tasks):
                for j in range(i + 1, self.num_tasks):
                    d_i = self.tasks[i].get("duration", 10.0)
                    d_j = self.tasks[j].get("duration", 10.0)
                    idx_i = self._var_idx(i, w)
                    idx_j = self._var_idx(j, w)
                    qubo.set_quadratic(idx_i, idx_j, lambda_balance * d_i * d_j / 100.0)

        return qubo
