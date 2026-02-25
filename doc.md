# Smart Fleet Optimization Framework  
## Objective: Improve Seat Utilization with Minimal Vehicle Trips

We structure the solution in three optimization layers:

1. Demand Forecasting  
2. Nightly Capacity Planning  
3. Real-Time Rolling Micro-Optimization  

---

# 1️⃣ Demand Forecasting Layer

## Purpose  
Predict shift-wise and route-wise transport demand for the upcoming day with uncertainty awareness.

---

## A. Data Layer

### Internal Data
- Historical employee login/logout requests  
- Shift timing distributions  
- Route/nodal point mapping  
- Historical seat utilization  
- Cancellation / no-show rates  
- Driver shift logs  

### External Signals
- Weekday / holiday calendar  
- Payroll cycle effects  
- Weather conditions  
- Office event schedules  
- Hybrid work policy signals  

**Granularity:**  
Shift × Route × Day-level data

---

## B. AI Modeling Layer

### Hierarchical Forecasting Framework

1. Total Daily Demand Prediction  
   - Ensemble model (e.g., Gradient Boosting + Temporal models)

2. Shift-Level Demand Allocation  
   - Conditional distribution modeling

3. Route-Level Distribution  
   - Spatial clustering + probabilistic allocation

### Output

\[
D_{s,r} = \text{Expected demand for shift s, route r}
\]

Model produces:
- Mean demand
- Confidence intervals
- Variance estimates for buffer planning

---

## C. Technical Outcomes

- Demand heatmap across shifts and routes  
- Variance-aware capacity planning inputs  
- Early identification of high-demand hotspots  
- Reduced planning uncertainty  

---

# 2️⃣ Nightly Capacity Planning Layer

## Purpose  
Pre-allocate vehicles across shifts and routes to minimize vehicle trips while maximizing seat utilization.

---

## A. Data Layer

Inputs:
- Forecasted demand \( D_{s,r} \)  
- Fleet inventory (vehicle capacity, type)  
- Driver availability and shift constraints  
- Route travel time matrix  
- Cost per vehicle trip  
- Driver rest constraints  
- SLA constraints (max ride time)  

---

## B. Optimization Modeling Layer

Two approaches evaluated:

---

### Approach 1: Structured Heuristic Allocation

- Demand-priority bucket formation  
- Greedy vehicle assignment  
- Rule-based vehicle reuse under rest constraints  
- Residual demand handling logic  

**Characteristics:**
- Fast execution  
- Highly scalable  
- No guaranteed optimality  

---

### Approach 2: MILP-Based Optimization

Decision Variables:

\[
x_{v,s,r} = \text{vehicle assignment variable}
\]

Objective:

\[
\text{Minimize total vehicle trips}
\]

Subject to:
- Demand satisfaction  
- Capacity constraints  
- Driver rest constraints  
- Shift compatibility constraints  
- SLA constraints  

Solver Options:
- OR-Tools  
- Gurobi  
- CPLEX  

**Characteristics:**
- Near-optimal allocation  
- Quantifiable optimality gap  
- Higher computational cost  

---

## C. Technical Outcomes

- Optimized vehicle allocation blueprint  
- Reduced empty-seat percentage  
- Increased cross-shift vehicle reuse  
- Lower projected daily transport cost  
- Pre-day allocation finalized before operations  

---

# 3️⃣ Real-Time Rolling Micro-Optimization Layer

## Purpose  
Continuously re-run allocation using actual booking inflow within operational windows.

---

## A. Data Layer

Live Inputs:
- Real-time booking inflow (Shift × Route)  
- Cancellations / no-shows  
- Vehicle GPS & availability status  
- Remaining seat capacity  
- Driver working hour status  
- Traffic conditions  
- SLA constraints  

Update Mechanism:
- Trigger-based (e.g., demand deviation threshold)  
- Or fixed interval re-optimization  

---

## B. Optimization Modeling Layer

### Rolling Horizon Re-Optimization

When actual demand deviates from forecast:

\[
D'_{s,r} = \text{Observed real demand}
\]

Re-solve allocation problem for upcoming windows.

Constraints:
- Already dispatched vehicles remain fixed  
- Demand updated with real values  
- Capacity and rest constraints enforced  
- SLA constraints maintained  

Decision Rule:
Minimize incremental vehicle deployment while maximizing occupancy.

Solver Strategy:
- Limit horizon to next 2–3 shifts  
- Warm-start using nightly allocation  
- Time-bound solver tolerance  

---

## C. Technical Outcomes

- Dynamic correction of forecast error  
- Reduced adhoc vehicle deployment  
- Improved real-time seat fill ratio  
- Controlled SLA adherence  
- Adaptive convergence toward cost minimum  

---

# Integrated System Flow

1. Forecast demand with uncertainty awareness  
2. Perform constraint-based nightly allocation  
3. Continuously re-optimize using real-time demand  

---

# Expected Business Impact

- 8–15% reduction in total vehicle trips  
- Improved average seat utilization  
- Lower cost per transported employee  
- Reduced manual operational intervention  
- Scalable and data-driven transport optimization  

---

# Positioning Statement

We model enterprise transport as a multi-period constrained optimization problem.  
By integrating probabilistic demand forecasting, nightly constraint-based allocation, and rolling horizon re-optimization, the system systematically reduces empty seats and minimizes total vehicle trips while preserving operational and SLA constraints.
