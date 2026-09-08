# Task: Simple Vacuum Cleaner Simulation
__Objective__: Create a simulation of a simple vacuum cleaner agent operating in a two-dimensional environment to clean dirty tiles.
Description:
1.	__Environment__:
 - A two-dimensional grid, for example, 5x5, where each cell can be either clean or dirty.
 - Initially, assign the "dirty" state to a few random cells.
 - The vacuum cleaner starts at a random position on the grid.
2.	__Vacuum Cleaner Actions__:
 - The vacuum cleaner can perform the following actions: suck (clean the current cell), move left, move right, move up, move down.
 - The vacuum cleaner operates based on simple reactive rules:
 - If the current cell is dirty, it cleans the cell (suck).
 - If the cell is clean, it moves in a random direction.
3.	__Vacuum Cleaner Goal__:
 - The ultimate goal is to reach a state where all cells are clean.
 - The task ends when the vacuum cleaner achieves this state.
__Hints for Developers__:
 - Start by creating the grid model and implementing the basic actions for the vacuum cleaner.
 - Implement the reactive logic according to the defined rules.
 - An optional final step could be to add a simple interface for visualizing the vacuum cleaner's actions.

 --- 
 # Updated
 ---

# CSCI 446 — Artificial Intelligence
## Vacuum World: Four-Phase Programming Assignment
### Montana Tech, Fall 2026

---

## Background

Before writing any code, understand the vocabulary you will use
throughout this assignment and throughout the course.

An **agent** is anything that perceives its **environment** through
**sensors** and acts upon that environment through **actuators**.

What the agent perceives at a single moment is called a **percept**.
The complete history of everything the agent has ever perceived is
called the **percept sequence**.

The agent's behavior is described by its **agent function** — a
mapping from every possible percept sequence to an action. In theory
this can be written as a lookup table. In practice the table is
infinite, so we write an **agent program** instead: concrete code
that computes the same mapping efficiently.

How well the agent performs is measured by a **performance measure**
designed by us, the engineers. This is an external standard — the
agent does not see it. It simply tells us whether the agent is
doing what we actually want it to do.

---

## The Environment

A two-dimensional grid of N×N cells. Each cell is either **Clean**
or **Dirty**. The vacuum cleaner agent occupies exactly one cell
at a time.

**What is always true across all phases:**

- Grid size: 5×5
- Each cell starts as Clean or Dirty (assigned randomly)
- The agent starts at a random position
- The agent occupies exactly one cell at a time
- The task ends when all cells are Clean

**What changes across phases:**

- What the agent can perceive (its sensors)
- What the agent remembers between turns (its internal state)
- How the agent decides what to do (its agent program)

---

## Phase 1 — Simple Reflex Agent in an Unobservable Environment

### What the agent perceives (Sensors)

At each time step the agent receives exactly one **percept**:

```
Percept:
  position  — the (x, y) coordinates of the current cell
  status    — "Dirty" or "Clean" for the current cell
```

The agent perceives **nothing else**. It does not know the status
of any other cell. It does not know whether there is a wall in any
direction. It does not know how many cells remain dirty. This
environment is **unobservable** with respect to everything except
the current cell.

### What the agent can do (Actuators)

At each time step the agent produces exactly one **action**:

```
Action:
  clean  — boolean: whether to clean the current cell this turn
  move   — one of: "Up", "Down", "Left", "Right"
```

Note that `clean` and `move` are independent decisions made in the
same turn. Cleaning is a reaction to the current percept. Movement
is a navigation strategy.

If the agent attempts to move outside the grid boundary, it stays
in place. It does not know this happened.

### Part A — Deterministic Agent

Implement an agent that moves according to a fixed priority order:
Right → Down → Left → Up. When it cannot move in the preferred
direction (because it stays in place), try the next direction in
the priority list.

The agent has no memory. Every decision is based solely on the
current percept. This is a **simple reflex agent**.

**Questions to answer in your report:**

1. Draw the agent's path on a 5×5 grid starting from position (0,0).
   Which cells are never visited?
2. Does this agent always clean every cell? Justify your answer.
3. What is the agent function for this agent?
   Can you write it as a table for the first three time steps?

### Part B — Random Agent

Implement an agent that cleans the current cell if dirty and moves
in a randomly chosen direction each turn.

This agent also has no memory. It is also a **simple reflex agent**.

**Questions to answer in your report:**

1. Run both agents (Part A and Part B) 200 times each on the same
   grid configuration. Record the performance measure for each run.
2. Which agent has a better average performance measure?
   Is this result surprising? Explain why.
3. Can the random agent guarantee that it will eventually clean
   every cell? Justify your answer mathematically or intuitively.

### Part C — Memory Agent

Implement an agent that remembers which cells it has already
visited. Use this memory to prefer unvisited cells when choosing
a direction.

This agent maintains an **internal state** between turns.
In R&N pseudocode notation, this internal state is declared as
`persistent`. In Python it is implemented as instance attributes
(`self.*`) initialized in the constructor.

The agent still receives the same percept as Parts A and B.
It has no bump sensor. If it attempts to move into a wall and
stays in place, it must detect this by inference:

> "I chose to move Right. My position did not change.
>  Therefore there is a wall to my right."

This inference is part of the agent's **transition model** —
its knowledge of how the world responds to actions.

When all neighboring cells have already been visited, the agent
must choose to revisit one. Explain in your report why this
situation occurs and how you handle it.

This is a **model-based reflex agent**.

**Questions to answer in your report:**

1. Compare the performance measure of Parts A, B, and C.
   Present results as a table with mean and standard deviation
   over 200 runs.
2. Identify a grid configuration where the memory agent gets
   stuck or performs poorly. Draw it.
3. What is the difference between the agent function and the
   agent program for your memory agent?
   Where does the agent program diverge from a simple lookup table?

### Performance Measure — Phase 1

You will measure agent performance using the following formula:

```
efficiency = total_steps / cells_cleaned
```

A lower score is better. If the agent does not clean all cells
within 500 steps, record the coverage percentage separately.

Also record for each run:
- Total steps taken
- Number of cells cleaned
- Maximum number of times any single cell was visited
- Whether the agent finished (cleaned all cells) within 500 steps

**Design question:**

Propose an alternative performance measure. Show a scenario where
your alternative gives a different ranking of the three agents than
the efficiency formula above. Which measure better reflects what
we actually want?

This question connects to the **value alignment problem**: the
performance measure we write into code must match what we truly
want the agent to achieve.

---

## Phase 2 — Model-Based Agent with Partial Observability

### What changes

The agent now has a range sensor. At each time step the percept
includes the status of all cells within a Manhattan distance of 2
from the agent's current position.

```
Percept:
  position      — (x, y) of current cell
  status        — status of current cell
  visible_cells — dictionary: {(x,y): "Dirty" or "Clean"}
                  for all cells within range 2
```

The agent still has no bump sensor. Everything else from Phase 1
remains the same.

### Task

Extend your memory agent from Phase 1 Part C to use
`visible_cells`. When the agent can see a dirty cell within range,
it should navigate towards it rather than exploring blindly.

### Questions to answer in your report

1. Compare performance at range = 0 (Phase 1C), range = 1,
   range = 2, range = 3. Present as a table over 200 runs.
2. At what range does improvement plateau? Why?
3. Draw two scenarios:
   a. A case where range = 2 helps significantly.
   b. A case where range = 2 provides no benefit.
4. Is this environment **fully observable**, **partially
   observable**, or **unobservable**? Justify using the formal
   definition from R&N Chapter 2.
5. Is this environment **static** or **dynamic**?
   Is it **deterministic** or **nondeterministic**?
   Is it **episodic** or **sequential**?

---

## Phase 3 — Search-Based Agent with Full Observability

### What changes

The agent now has full visibility. The percept includes the
complete state of the grid.

```
Percept:
  position      — (x, y) of current cell
  status        — status of current cell
  visible_cells — dictionary: {(x,y): status} for ALL cells
```

### Formal problem definition

Before implementing any search algorithm, write down the formal
definition of this problem as a **search problem**:

```
State:
  A complete description of the world at one point in time.
  What information must a state contain?

Initial state:
  The state the agent starts in.

Actions(state):
  The set of actions available in a given state.

Transition model — Result(state, action):
  The state that results from taking action in state.

Goal test — Is-Goal(state):
  Returns True if state is a goal state.

Action cost:
  The cost of taking one action.
```

Fill in each component for the vacuum world.
How many distinct states exist in a 5×5 grid?

### Task A — Breadth-First Search

Implement BFS. The agent computes a complete plan before taking
any action, then executes the plan step by step.

Properties to verify in your report:
- Is BFS **complete**? (Does it always find a solution if one exists?)
- Is BFS **cost-optimal**? (Does it find the shortest solution?)
- What is the **time complexity** in terms of b (branching factor)
  and d (depth of solution)?
- What is the **space complexity**?

### Task B — Depth-First Search

Implement DFS using a LIFO frontier (stack).

Compare with BFS:
- Does DFS find the same solution as BFS?
- Is DFS cost-optimal?
- How does memory usage compare?

### Task C — Comparison

Run BFS and DFS on 100 random grid configurations.
For each run record:
- Solution length (number of actions)
- Number of nodes expanded
- Whether a solution was found

Present results as a table. Explain any differences.

---

## Phase 4 — A* Search with Heuristic Function

### Background

A **heuristic function** h(n) estimates the cost of the cheapest
path from state n to a goal state. It is the agent's internal
estimate of how far it is from "happiness" — from the goal.

This connects to the **utility function** from R&N Chapter 2:

> The heuristic function is the utility function viewed from
> the perspective of search. Where utility measures how good
> a state is, the heuristic measures how far we are from
> the best possible state.

A heuristic is **admissible** if it never overestimates the
true cost to reach the goal:

```
h(n) ≤ h*(n)   for all nodes n
```

where h*(n) is the true optimal cost from n to the nearest goal.

An admissible heuristic guarantees that A* finds an optimal
solution.

### Task A — Simple Heuristic

Implement A* search using the following heuristic:

```
h(n) = number of dirty cells remaining in state n
```

Prove that this heuristic is admissible. Write the proof in your
report in plain English — no formal notation required.

### Task B — Better Heuristic

Design and implement a second heuristic that is still admissible
but provides more information than h1:

```
h(n) = number of dirty cells + distance to nearest dirty cell
```

Prove admissibility for this heuristic as well.

### Task C — Comparison

Run all four agents (BFS, DFS, A* with h1, A* with h2) on 100
random grid configurations. Record:

| Agent          | Solution length | Nodes expanded | Finished |
|----------------|-----------------|----------------|----------|
| BFS            |                 |                |          |
| DFS            |                 |                |          |
| A* (h1)        |                 |                |          |
| A* (h2)        |                 |                |          |

**Questions to answer in your report:**

1. BFS and both A* variants all find optimal solutions.
   Why does A* expand fewer nodes than BFS?
2. What does "nodes expanded" measure? Why do we care about it?
3. h2 dominates h1. What does dominance mean formally?
   Show this in your comparison table.
4. Design a third heuristic. Is it admissible?
   Does it dominate h2? Test it experimentally.

---

## Vocabulary Reference

Use the following terms correctly in your report.
Each term has a precise meaning — do not use it loosely.

| Term                    | Definition                                               |
|-------------------------|----------------------------------------------------------|
| Agent                   | Anything that perceives and acts                         |
| Percept                 | What the agent perceives at one moment                   |
| Percept sequence        | Complete history of all percepts                         |
| Sensor                  | Hardware/software that produces percepts                 |
| Actuator                | Hardware/software that executes actions                  |
| Agent function          | Complete mapping: percept sequence → action              |
| Agent program           | Concrete implementation of the agent function            |
| Performance measure     | External measure of agent quality (designed by us)       |
| Utility function        | Internal measure of state quality (used by agent)        |
| Internal state          | Information the agent stores between turns               |
| Transition model        | Knowledge of how actions change the world                |
| Sensor model            | Knowledge of how world state maps to percepts            |
| Simple reflex agent     | Decides based only on current percept                    |
| Model-based agent       | Maintains internal state to track unobserved world       |
| Fully observable        | Agent can perceive complete world state                  |
| Partially observable    | Agent can perceive only part of world state              |
| Deterministic           | Next state fully determined by current state and action  |
| State space             | Set of all possible states                               |
| Search tree             | Tree of paths through state space                        |
| Frontier                | Nodes generated but not yet expanded                     |
| Admissible heuristic    | h(n) never overestimates true cost to goal               |
| Value alignment problem | Gap between what we specify and what we actually want    |

---

## Grading

| Component                          | Points |
|------------------------------------|--------|
| Phase 1A — Deterministic agent     | 10     |
| Phase 1B — Random agent            | 10     |
| Phase 1C — Memory agent            | 15     |
| Phase 2 — Partial observability    | 15     |
| Phase 3 — BFS and DFS              | 20     |
| Phase 4 — A* with heuristics       | 20     |
| Report questions (all phases)      | 10     |
| **Total**                          | **100**|

---

## Required Comment Header

Files without the header receive zero points.
