#!/bin/bash

PYTHONPATH=. python -m cProfile -o temp.dat gomoku/test_game.py
snakeviz temp.dat

