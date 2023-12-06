#!/usr/bin/env bash

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