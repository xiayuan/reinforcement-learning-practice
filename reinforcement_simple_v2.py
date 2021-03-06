#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pylab as plt
import networkx as nx


# map cell to cell, add circular cell to goal point
points_list = [(0, 1), (1, 5), (5, 6), (5, 4), (1, 2), (2, 3), (2, 7)]

goal = 7

bees = [2]
smoke = [4, 5, 6]

G = nx.Graph()
G.add_edges_from(points_list)
mapping = {
    0: 'Start',
    1: '1',
    2: '2 - Bees',
    3: '3',
    4: '4 - Smoke',
    5: '5 - Smoke',
    6: '6 - Smoke',
    7: '7 - Beehive'}
H = nx.relabel_nodes(G, mapping)
pos = nx.spring_layout(H)
nx.draw_networkx_nodes(
    H,
    pos,
    node_size=[
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200])
nx.draw_networkx_edges(H, pos)
nx.draw_networkx_labels(H, pos)
# plt.show()

MATRIX_SIZE = 8

# learning parameter
gamma = 0.8

initial_state = 1

# re-initialize the matrices for new run
Q = np.matrix(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))

# create matrix x*y
R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
R *= -1

# assign zeros to paths and 100 to goal-reaching point
for point in points_list:
    print(point)
    if point[1] == goal:
        R[point] = 100
    else:
        R[point] = 0

    if point[0] == goal:
        R[point[::-1]] = 100
    else:
        # reverse of point
        R[point[::-1]] = 0

# add goal point round trip
R[goal, goal] = 100

print R


enviro_bees = np.matrix(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))
enviro_smoke = np.matrix(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))


def available_actions(state):
    current_state_row = R[state, ]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act


available_act = available_actions(initial_state)


def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act, 1))
    return next_action


def collect_environmental_data(action):
    found = []
    if action in bees:
        found.append('b')

    if action in smoke:
        found.append('s')
    return (found)


action = sample_next_action(available_act)


def update(current_state, action, gamma):
    max_index = np.where(Q[action, ] == np.max(Q[action, ]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    Q[current_state, action] = R[current_state, action] + gamma * max_value
    print('max_value', R[current_state, action] + gamma * max_value)

    environment = collect_environmental_data(action)
    if 'b' in environment:
        enviro_bees[current_state, action] += 1

    if 's' in environment:
        enviro_smoke[current_state, action] += 1

    if (np.max(Q) > 0):
        return (np.sum(Q / np.max(Q) * 100))
    else:
        return (0)


update(initial_state, action, gamma)

scores = []
for i in range(700):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    score = update(current_state, action, gamma)

# print environmental matrices
print('Bees Found')
print(enviro_bees)
print('Smoke Found')
print(enviro_smoke)
