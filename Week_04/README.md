#### DFS代码模版

```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    		return 

		visited.add(node) 

		# process current node here. 
		...
		for next_node in node.children(): 
			if next_node not in visited: 
				dfs(next_node, visited)
```

#### BFS代码模版

```python
def BFS(graph, start, end):
    visited = set()
		queue = [] 
		queue.append([start]) 
    
		while queue: 
			node = queue.pop() 
			visited.add(node)
      
			process(node) 
			nodes = generate_related_nodes(node) 
			queue.push(nodes)
	# other processing work 
```

#### 写在后面的话

​		随着课程的不断深入，渐渐的有点跟不上，理解起来有点吃力。到现在，接触到的解题方式也有些了，很容易产生混乱。leetcode题解是会有多种方式去解决，目前的追求只是力求记住一种比较优的解题方法。剩下的等掌握再说吧。说起来还是基础差。嗯坚持✊

