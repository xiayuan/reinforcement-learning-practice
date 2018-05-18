# reinforcement-learning-practice
reinforcement-learning practice

在Pong这个案例
* supervised learning在每一个action上的标签， up/down 是否正确；
* reinforcement learning上，由于在game结束之前，每一个action的label是不知道的，因此，RL在这里先假设一个action的分布（比如，up:0.7,down:0.3)，然后通过这个分布采样获取action，比如得到up， 那么认为此时的label为+1，并记录相应的梯度，用于反向传播。这样在game结束之后，每一个action都会有一个label，虽然这个label是采样得到的，但可以根据game最终结果来更新这一系列的动作。


Example:

100场game，每一场200 frame，一共20000个action，则需要label这20000个action，哪些是good or bad, 如果
* win 12场， 那么 12 x 200 = 2400 good actions -> encourage
* lose 88场， 那么 88 x 200 = 17600 bad actions -> discourage


supervised learning: 

<a href="https://www.codecogs.com/eqnedit.php?latex=maximize&space;\sum_{i}logp(y_i|x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?maximize&space;\sum_{i}logp(y_i|x_i)" title="maximize \sum_{i}logp(y_i|x_i)" /></a>

RL:

<a href="https://www.codecogs.com/eqnedit.php?latex=maximize&space;\sum_{i}A_ilogp(\widehat{y}_i|x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?maximize&space;\sum_{i}A_ilogp(\widehat{y}_i|x_i)" title="maximize \sum_{i}A_ilogp(\widehat{y}_i|x_i)" /></a>

A_i: advantages, in Pong Game, (+1, -1)

yhat_i, fake label, action sample from distribution

1) label y_i is fake label, which is sample from distribution.

2) 根据game最终的结果，来修改loss值

episode  | from sample | loss | RL loss
  ------------- | -------------|------------- | -------------
s1  | y1 |  logp(y1\|x1) | a_1 logp(y1\|x1)
s2  | y2 |  logp(y2\|x2) | a_2 logp(y2\|x2)
...  | ... | ... | ...
sn  | yn |  logp(yn\|xn) | a_n logp(yn\|xn)

In general RL, receive some reward r_t at every time step
最终结果需要计算折现率γ  \[a1,a2,...,an\]

 
 
 
 
