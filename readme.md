# Game of life

##Usage


```python
import Board
b = Board()
b.seed([(1,1),(1,2),(2,1),(2,2)])
b.tick()
b.state # to get state new state
```

Custom Conditions for Birth and Survival could be given

```python
import Board
b = Board((3,4),(3,4)) # first tuple contains the birth conditions and second tuple contains the survival conditions

b.seed([(1,1),(1,2),(2,1),(2,2)])
b.tick()
b.state # to get state the state according to new conditions

```

##Testing code
Run the following to test if everything is working fine, the test cases are for boat, block , oscillator and toad pattern.

```sh 
python board.py

```


