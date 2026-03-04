# Do Fundamentals Explain Historic AI Valuations?

**RQ: Has openness declined as models get larger?**

## Variables

### Dependent Variable (Openness)

- Model accessibility (open weights vs. not), OR training code accessibility
- Converted to binary:
  - `1` = Open weights
  - `0` = Closed / API-only / Unreleased

### Main Independent Variables (Model Size)

- Training compute (FLOP)
- Parameters
- Optional: Training compute cost (USD) — low coverage

> Use log transformations.

### Time Control

- Publication date → extract Year
- To test trend over time.

### Control Variables

- Organization categorization (Industry vs. Academia)
- Domain (e.g., Language vs. other)
- Frontier model (boolean)
- Country

## Core Model

$$\text{Open}_i = f(\log \text{Compute}_i,\ \log \text{Parameters}_i,\ \text{Year}_i,\ \text{OrgType}_i)$$

Logistic regression.
