# knowledge-session-software-testing

Knowledge session demo about software testing.

The following topics will be explained/discussed using this example project:

* test arrangement
  * given, when, then / arrange, act, assert
* fixtures and test setup
* line coverage vs functional coverage
* solitary vs sociable
* stubs vs mocks

# Installation

```shell
pip install -r requirements
pip install -e .
```

# Run tests

```shell
# without coverage report
pytest --cov=app --verbose test
# with html report
pytest --cov=app --cov-report=html --verbose test
```

# Theme

This example project is build using a somewhat relevant theme for the energy sector. The theme will be congestion management on the electricity grid. The following rules apply:


* customer
  * has a contract type
  * makes a capacity request (for given days and power)
* capacity allocator
  * accepts or denies the capacity request of the customer
  * uses the contract inspector
* contract inspector
  * inspects the contract to determine if the requested power is allowed

## Contract types

* contract type A
    * always firm capacity is allowed
    * non-firm only on sat or sun
* contract type B
    * always firm capacity is allowed
    * non-firm when total capacity is available
