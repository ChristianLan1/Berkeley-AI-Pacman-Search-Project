# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()
    Action = []
    Cost = []
    frontier.push((problem.getStartState(),Action,Cost))
    visited = {}
    visited[problem.getStartState()] = True
    
    '''currentAction = {}'''
    while not frontier.isEmpty():
        '''print "isEmpty", frontier.isEmpty()'''
        current = frontier.pop()
        '''print "current", current'''
        currentState = current[0]
        currentAction = current[1]
        
        '''print "currentAction0", Action'''
        '''currentAction[current[1]] = current[1]'''
        currentCost = current[2]
        
        '''print " currentAction", currentAction '''
        '''if problem.isGoalState(currentState):
            return currentAction'''
        visited[currentState] = True
        if problem.isGoalState(currentState):
                    '''frontier.push((next[0],currentAction+[next[1]],next[2]))'''

                    '''print "next[1]", next[1]
                    print "currentAction", currentAction+[next[1]]'''
                    return currentAction
        for next in problem.getSuccessors(currentState):
            
            if next[0] not in visited:
                
                '''print "next", next[0]'''
                
                frontier.push((next[0],currentAction+[next[1]],[next[2]]))
                '''visited[next[0]] = True'''
    return []
    
            
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print"bfs"
    frontier = util.Queue()
    Action = []
    Cost = []
    frontier.push((problem.getStartState(),Action,Cost))
    visited = []#cannot use list cause agent will pass two parameter
    #visited = {}
    visited.extend(problem.getStartState())
    #visited[problem.getStartState()] = True
    
    currentAction = {}
    while not frontier.isEmpty():
        '''print "isEmpty", frontier.isEmpty()'''
        current = frontier.pop()
        #print "current", current
        currentState = current[0]
        currentAction = current[1]
        
        #print "currentAction0", currentAction
        '''currentAction[current[1]] = current[1]'''
        currentCost = current[2]
        #print "currentState", currentState
        '''visited[currentState] = True'''
        
        if problem.isGoalState(currentState):            
                '''print "next[1]", next[1]
                print "currentAction", currentAction+[next[1]]'''
                """print"action", currentAction"""

                return currentAction
        '''print " currentAction", currentAction '''
        for next in problem.getSuccessors(currentState):
            #print"next00", next[0][0]
            #print"visited", visited
            #print"nextinBFS", next[0]
            if next[0] not in visited:
                
                #print "next", next[0]
                
                frontier.push((next[0],currentAction+[next[1]],next[2]))
                '''print"action", currentAction+[next[1]]'''
                #visited[next[0]] = True
                visited.append(next[0])
            """else:
                print"continue"
                if problem.isGoalState(currentState):
                    return currentAction
                continue"""
            #print"wrongbfs"
    print"return"

    return []
            

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
            

    Cost = []
    priority = 0
    frontier = util.PriorityQueue()
    Action = []
    
    frontier.push((problem.getStartState(),Action,Cost),priority)
    visited = {}
    costSoFar = {}
    #visited[problem.getStartState()] = True
    
    currentAction = {}
    num = 0
    
    while not frontier.isEmpty():
        
        '''priority = 0'''
        '''print "isEmpty", frontier.isEmpty()'''
        current = frontier.pop()
        
        currentState = current[0]
        #print "current", currentState
        currentAction = current[1]
        
        '''print "currentAction0", currentAction'''
        '''currentAction[current[1]] = current[1]'''
        currentCost = current[2]
        for cost in currentCost:
            num =float(cost)
        costSoFar[currentState] = num
        
        #print"firstcostsofar", costSoFar[currentState]
        #print"cost", currentCost
        '''print "printCost", currentCost'''
        '''print " currentAction", currentAction '''
        if problem.isGoalState(currentState):
                    
                '''print "next[1]", next[1]'''
                '''print "currentCost", currentCost'''
                return currentAction
            
        if currentState not in visited:
            #visited[currentState] = True
            for next in problem.getSuccessors(currentState):
                #print"costsofar", costSoFar[currentState]
                newCost = costSoFar[currentState]+next[2]
                
            
            
                if next[0] not in visited or newCost < costSoFar[next[0]]:
                    costSoFar[next[2]] = newCost
                    
                
                
                    '''print "next", next'''
                
                    ''' print "next2", next[2]'''
                    '''print "currentCost", currentCost'''
                
                    frontier.push((next[0],currentAction+[next[1]],currentCost+[next[2]]),problem.getCostOfActions(currentAction+[next[1]]))
        visited[currentState] = True#if put inside of the loop last problem wrong
            
    return []
      
    
            

    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    Cost = []
    priority = 0
    frontier = util.PriorityQueue()
    Action = []
    
    frontier.push((problem.getStartState(),Action,Cost),priority)
    visited = []
    #visited[problem.getStartState()] = True
    
    currentAction = {}
    costSoFar = {}
    num = 0
    isStateList = False
    
    while not frontier.isEmpty():
        '''priority = 0'''
        '''print "isEmpty", frontier.isEmpty()'''
        current = frontier.pop()
        #print"current in astar", current
        currentState = current[0]
        #print "current", currentState
        currentAction = current[1]
        
        '''print "currentAction0", currentAction'''
        '''currentAction[current[1]] = current[1]'''
        currentCost = current[2]
        for cost in currentCost:
            num =float(cost)
        #print"length of state", len(currentState)
        #if type(current[0]) is list:
        #print"type cost", type(currentState)
        if  isinstance(currentState,tuple) or isinstance(currentState,list):
            isStateList = True
            costSoFar[currentState[0]] = num
        else:
            #print"currentState",currentState
            #print"type", type(currentState)
            costSoFar[currentState] = num
        
        
        '''print "printCost", currentCost'''
        '''print " currentAction", currentAction '''
        if problem.isGoalState(currentState):
                    
                '''print "next[1]", next[1]'''
                '''print "currentCost", currentCost'''
                return currentAction
            
        if currentState not in visited:
            #visited[currentState] = True
            for next in problem.getSuccessors(currentState):
                if isStateList:
                    newCost = costSoFar[currentState[0]]+next[2]
                    if next[0] not in visited or newCost < costSoFar[next[0][0]]:
                        costSoFar[next[2]] = newCost
                
                
                        '''print "next in a star", next'''
                
                        ''' print "next2", next[2]'''
                        #print "currentCost", currentCost
                        priority = problem.getCostOfActions(currentAction+[next[1]]) + heuristic(next[0],problem)                 
                        frontier.push((next[0],currentAction+[next[1]],currentCost+[next[2]]),priority)
                else:
                    
                    newCost = costSoFar[currentState]+next[2]
                    if next[0] not in visited or newCost < costSoFar[next[0]]:
                        costSoFar[next[2]] = newCost
                
                
                        '''print "next in a star", next'''
                
                        ''' print "next2", next[2]'''
                        #print "currentCost", currentCost
                        priority = problem.getCostOfActions(currentAction+[next[1]]) + heuristic(next[0],problem)                 
                        frontier.push((next[0],currentAction+[next[1]],currentCost+[next[2]]),priority)
            
                
                """if next[0] not in visited or newCost < costSoFar[next[0]]:
                    costSoFar[next[2]] = newCost
                
                
                    '''print "next in a star", next'''
                
                    ''' print "next2", next[2]'''
                    #print "currentCost", currentCost
                    priority = problem.getCostOfActions(currentAction+[next[1]]) + heuristic(next[0],problem)                 
                    frontier.push((next[0],currentAction+[next[1]],currentCost+[next[2]]),priority)"""
        #visited[currentState] = True#if put inside of the loop last problem wrong
        visited.append(currentState)    
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
