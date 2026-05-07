---
title: "Continuous Delivery"
tags: [devops, software-delivery, automation, lean, cicd]
related:
- dora-metrics
- devops
- lean-software-development
- dark-factory
- lean-production
source: research/raw/continuous-delivery.md
---
# Continuous Delivery

## Summary

Continuous Delivery is the software engineering approach where every code change that passes automated tests is automatically built, tested, and prepared for release to production. The system is always in a deployable state. This is the software equivalent of just-in-time production: deploy only what is validated, when it is ready, in small increments. Key practices include trunk-based development, feature flags, automated testing pipelines, blue-green or canary deployments, and deployment on demand rather than scheduled windows. Continuous Delivery directly improves DORA metrics: higher deployment frequency, lower lead time for changes, and lower change failure rate through smaller, more frequent releases. In agent systems, CD is the deployment pipeline that enables autonomous development — agents commit code, the pipeline validates it, and the system deploys without human intervention.

## Key Claims

- Every change that passes automated tests should be deployable at any point
- Smaller, more frequent releases reduce risk and improve feedback loops
- Feature flags decouple deployment from release, enabling continuous delivery
- In dark-factory agent systems, CD is the pipeline that agents use for autonomous deployment

## Related

- [[dora-metrics]] — measures the effectiveness of CD pipelines
- [[devops]] — CD is a core DevOps practice
- [[lean-software-development]] — CD enables flow and eliminates deployment waste
- [[dark-factory]] — CD is the deployment pipeline that agents use autonomously
- [[lean-production]] — just-in-time production is the manufacturing parallel
