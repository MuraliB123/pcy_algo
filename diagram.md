## End-to-End System Flow

flowchart TD

A[Historical Data + External Signals] --> B[Demand Forecasting Engine]

B --> C[Shift × Route Demand Forecast D_s,r]

C --> D[Nightly Capacity Planning Engine]

D --> E[Initial Vehicle Allocation Plan]

E --> F[Operational Day Begins]

F --> G[Real-Time Booking Stream]

G --> H{Demand Deviation?}

H -- No --> I[Continue Monitoring]

H -- Yes --> J[Rolling Horizon Re-Optimization]

J --> K[Updated Allocation Plan]

K --> L[Dispatch / Reassign Vehicles]

L --> G

## Flowchart: Hierarchical Forecasting
flowchart TD

A[Historical Transport Data] --> B[Feature Engineering]
C[External Factors] --> B

B --> D[Total Daily Demand Model]

D --> E[Shift-Level Distribution Model]

E --> F[Route-Level Allocation Model]

F --> G[Final Forecast Matrix D_s,r]

## Flowchart: Nightly Optimization

flowchart TD

A[Forecast Demand D_s,r] --> B[Fleet Inventory Data]
B --> C[Driver Availability Data]
C --> D[Constraint Builder]

D --> E{Optimization Type}

E -- Heuristic --> F[Greedy Allocation Engine]
E -- MILP --> G[Solver Engine]

F --> H[Vehicle Allocation Plan]
G --> H

H --> I[Store Plan for Next Day]

## Flowchart: Rolling Horizon Adjustment

flowchart TD

A[Real-Time Booking Stream] --> B[Update Demand Matrix D'_s,r]

B --> C{Deviation Threshold Breached?}

C -- No --> D[Continue Monitoring]

C -- Yes --> E[Lock Dispatched Vehicles]

E --> F[Rebuild Partial Optimization Model]

F --> G[Re-Solve for Upcoming Shifts]

G --> H[Updated Allocation Plan]

H --> I[Dispatch Adjustments] 

## Flowchart: Residual Insertion

flowchart TD

A[Residual Demand 2-3 Employees] --> B[Find Nearby Active Routes]

B --> C[Compute Incremental Cost]

C --> D{Feasible under SLA?}

D -- Yes --> E[Insert into Existing Vehicle]

D -- No --> F[Deploy New Vehicle]

