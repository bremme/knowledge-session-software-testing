# knowledge-session-software-testing

Knowledge session demo about software testing.

The following topics will be explained/discussed using this example project:

* test arrangement
  * given, when, then / arrange, act, assert
* fixtures and test setup
* line coverage vs functional coverage
* solitary vs sociable
* stubs vs mocks (test doubles)

# Installation

```shell
pip install -r requirements
pip install -e .
```

# Setup test folder

```shell
# setup test directories
mkdir -p test/capacity test/contract

# setup python packages
touch \
  test/__init__.py \
  test/capacity/__init__.py \
  test/contract/__init__.py

# setup empty tests
touch \
  test/capacity/test_capacity_allocator.py \
  test/contract/test_inspector.py \
  test/contract/test_repository.py \
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

# More on concepts

**solitary test**

* pro
  * isolation
  * fast
  * easy to find issues
* con
  * can be more brittle (when depending too much on implementation)

**sociable tests**

* integration
* usually fast
* generally less dependent on the implementation / brittle
* might be harder to debug

> Take away, if the sociable / integration test has the same coverage using less loc compared to individual solitary test -> choose the sociable tests.

**mocks**

* use when order and arguments of calls are important

**stubs**

* simple controlled output

# Further reading

* https://martinfowler.com/bliki/UnitTest.html
* https://martinfowler.com/bliki/TestDouble.html