# In this exercise we have a simple INCREMENTER, which takes a 4-bit integer
# as input (i0, i1, i2, i3), of which i0 is the least-significant bit (LSB)
# and i3 is the most-significant bit (MSB).

# The incrementer outputs a 4-bit integer (o0, o1, o2, o3) and a carry bit.

# The task is to encode the circuit in the propositional logic.

# i0, i1, i2 and i3 are input variables.
# o0, o1, o2 and o3 are output variables.
# a1, a2 and a3 are intermediate values computed by the AND-gates.

# Let's begin the exercise by defining the variables.

variables i0,i1,i2,i3;
variables o0,o1,o2,o3;
variables a1,a2,a3;
variables c;

# Let's proceed to propositional formulas.

a1 <-> (i0 and i1);
a2 <-> (a1 and i2);
a3 <-> (a2 and i3);
o0 <-> not(i0); # This is the one that was modified.
o1 <-> (i0 xor i1);
o2 <-> (a1 xor i2);
o3 <-> (a2 xor i3);
c <-> (a3);

# Before modifying line 25:

# With the previous lines of code, the passed tests were (34/46):
# Tests 6, 8-9, 11-32, 34-42

# Failed tests were (12/46): Tests 1-5, 7, 10, 33, 43-46

# Let's see should we include new formulas or modify the old ones.

# EDIT: I only needed to add the NOT-gate to line 25.