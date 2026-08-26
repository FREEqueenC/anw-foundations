"""
ANW Foundations - Quantum and Resource Oracle Verification Demo
File: anw_quantum/demo.py
"""

import sys

# Ensure UTF-8 output encoding for terminal compatibility
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from anw_quantum.optimizer import (
    QUBOProblem,
    QuantumInspiredAnnealer,
    LevityLiquidityOptimizer,
    AgentTaskScheduler
)
from anw_quantum.costing_oracle import (
    BloqSignature,
    Register,
    ComputationalBloq,
    ResourceCostOracle,
    StandardBloqs
)


def run_quantum_optimization_demo():
    print("=" * 60)
    print("[PILLAR 1] QUANTUM-INSPIRED OPTIMIZATION DEMO")
    print("=" * 60)

    # 1. Levity Protocol LP Optimization
    price_bins = [0.92, 0.96, 1.00, 1.04, 1.08, 1.12]
    volumes = [50000.0, 120000.0, 350000.0, 280000.0, 95000.0, 40000.0]
    lp_opt = LevityLiquidityOptimizer(price_bins, volumes, volatility=0.35)
    qubo_lp = lp_opt.build_qubo(max_active_bins=3)

    annealer_lp = QuantumInspiredAnnealer(qubo_lp, num_trotter_replicas=8, num_sweeps=300)
    result_lp = annealer_lp.solve(seed=42)

    print(f"\n[Levity LP Optimization Result]")
    print(f"Target Active Bands: 3 / Available: {len(price_bins)}")
    print(f"Optimal Allocation Vector: {result_lp['optimal_state']}")
    print(f"Selected Price Points: {[price_bins[i] for i, v in enumerate(result_lp['optimal_state']) if v == 1]}")
    print(f"Minimal Energy (Hamiltonian Cost): {result_lp['optimal_energy']:.4f}")

    # 2. NICOLE Multi-Agent Task Allocation
    tasks = [
        {"name": "ZK State Proof Generation", "duration": 45.0},
        {"name": "Sub-agent Code Synthesis", "duration": 25.0},
        {"name": "On-Chain Base Settlement", "duration": 15.0},
        {"name": "Memory Resonance Sync", "duration": 30.0}
    ]
    scheduler = AgentTaskScheduler(tasks, num_workers=2)
    qubo_sched = scheduler.build_qubo()
    annealer_sched = QuantumInspiredAnnealer(qubo_sched, num_trotter_replicas=6, num_sweeps=400)
    result_sched = annealer_sched.solve(seed=1337)

    print(f"\n[NICOLE Agent Task Scheduling Result]")
    print(f"Optimal State Vector: {result_sched['optimal_state']}")
    print(f"Optimal Schedule Energy: {result_sched['optimal_energy']:.4f}")


def run_resource_costing_demo():
    print("\n" + "=" * 60)
    print("[PILLAR 2] QUALTRAN-INSPIRED RESOURCE COSTING ORACLE")
    print("=" * 60)

    oracle = ResourceCostOracle(eth_price_usd=3400.0, base_gas_price_gwei=0.015)

    # Construct a Composite Smart Contract Pipeline:
    # A decentralized Oracle verifying 2 signatures, 1 Poseidon Hash, and 1 Levity Swap
    root_sig = BloqSignature([Register("bundle_payload", 1024)])
    bundle_bloq = ComputationalBloq(
        name="ANW_Verified_Oracle_Settlement",
        signature=root_sig,
        evm_gas=15000,
        sstore_slots=1,
        cadence_computation=50
    )

    bundle_bloq.add_sub_bloq(StandardBloqs.ecdsa_verify(), count=2)
    bundle_bloq.add_sub_bloq(StandardBloqs.poseidon_hash(), count=1)
    bundle_bloq.add_sub_bloq(StandardBloqs.levity_token_swap(), count=1)
    bundle_bloq.add_sub_bloq(StandardBloqs.qrom_lookup(table_size=32, bit_width=64), count=1)

    cost_report = oracle.cost(bundle_bloq)

    print(f"\nTarget Architecture: {cost_report['root_bloq']}")
    print(f"Decomposed Subroutines: {cost_report['call_counts']}")
    print("\n--- Cross-Platform Resource Breakdown ---")
    print(f"1. Base Mainnet / EVM:")
    print(f"   - Total Gas: {cost_report['evm']['total_gas']:,} units")
    print(f"   - SSTORE / SLOAD Slots: {cost_report['evm']['sstore_slots']} write / {cost_report['evm']['sload_slots']} read")
    print(f"   - Estimated USD Cost on Base: ${cost_report['evm']['estimated_usd_base']:.6f}")

    print(f"\n2. Flow / Cadence Engine:")
    print(f"   - Computation Units: {cost_report['flow_cadence']['computation_units']}")
    print(f"   - Within Cadence Execution Limit (9999): {cost_report['flow_cadence']['within_limit']}")

    print(f"\n3. Zero-Knowledge Circuit:")
    print(f"   - R1CS Constraints: {cost_report['zk_circuits']['r1cs_constraints']:,}")
    print(f"   - PlonK Custom Gates: {cost_report['zk_circuits']['plonk_gates']:,}")
    print(f"   - Est. Prover Generation Time: {cost_report['zk_circuits']['estimated_prover_time_s']:.3f}s")

    print(f"\n4. Fault-Tolerant Quantum (FTQC / Qualtran Model):")
    print(f"   - T-Gate Count: {cost_report['quantum_fault_tolerant']['t_gate_count']:,}")
    print(f"   - Toffoli Count: {cost_report['quantum_fault_tolerant']['toffoli_count']:,}")
    print(f"   - Logical Qubit Footprint: {cost_report['quantum_fault_tolerant']['logical_qubits']} qubits")
    print(f"   - Surface Code Spacetime Volume: {cost_report['quantum_fault_tolerant']['spacetime_volume']:,} qubit-cycles")


if __name__ == "__main__":
    run_quantum_optimization_demo()
    run_resource_costing_demo()
