# Cloud Cost Optimization Framework for SMEs

A modular, layered framework that ingests cloud billing data, analyzes
utilization patterns, and generates explainable cost-reduction
recommendations for small and medium-sized enterprises.

## Architecture

Five primary layers: Data Ingestion, Data Processing, Analysis Engine,
Recommendation Engine, Presentation Layer — supported by cross-cutting
modules for Authentication and Audit Logging.

## Branching Strategy

| Branch | Purpose |
|---|---|
| `main` | Production-ready, deliverable code |
| `develop` | Integration branch for ongoing work |
| `feature/*` | Isolated feature development |
| `docs/*` | Documentation-only changes |

## Commit Convention

`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`