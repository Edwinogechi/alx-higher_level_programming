#!/usr/bin/env python3
bytecode = __import__('102-magic_calculation').magic_calculation
import dis
dis.dis(bytecode)
